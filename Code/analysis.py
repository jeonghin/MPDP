#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Jeong Hin Chin
# Created Date: Nov 15, 2023
# Last Edited : Dec 2, 2023
# version     : '1.0'
# ---------------------------------------------------------------------------

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import requests
from openai import OpenAI
import dash_bootstrap_components as dbc
import pickle

####################################################
#                       GPT                        #
####################################################
API_KEY = "Your Key here"
client = OpenAI(api_key=API_KEY)


####################################################
#                 Machine Learning                 #
####################################################

candidate = pd.read_csv("Data/candidates_ge15.csv")
candidate.fillna(candidate.age.mean(), inplace=True)
census = pd.read_csv("Data/census_parlimen.csv")
census.fillna(census.sme_small.mean(), inplace=True)

merged_df = candidate.merge(census, on=["state", "parlimen"], how="left")

# Dropping votes, result_desc, and new_mp
merged_df = merged_df.drop(
    [
        "state",
        "name",
        "parlimen",
        "name_display",
        "votes",
        "result_desc",
        "new_mp",
        "code_state",
        "code_parlimen",
        "year",
    ],
    axis=1,
)

gender_mapping = {"male": 1, "female": 0}
ethnicity_mapping = {"bumiputera": 1, "chinese": 2, "indian": 3, "other": 4}
party_mapping = {
    party: index + 1 for index, party in enumerate(merged_df["party"].unique().tolist())
}
unique_parlimen_codes = candidate["parlimen"].unique()
merged_df["sex"] = merged_df["sex"].map(gender_mapping)
merged_df["ethnicity"] = merged_df["ethnicity"].map(ethnicity_mapping)
merged_df["party"] = merged_df["party"].map(party_mapping)

# Training the RandomForestClassifier
target_column = "result"

# Define features (X) and target (y)
X = merged_df.drop(target_column, axis=1)
y = merged_df[target_column]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123
)

with open("ML.pkl", "rb") as f:
    rf_classifier = pickle.load(f)


####################################################
#                       Dash                       #
####################################################

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        # Title
        html.H1(
            "Malaysian Political Dynamics Predictor (MPDP)",
            className="my-3 text-center",
        ),
        # Input form with padding
        dbc.Card(
            dbc.CardBody(
                [
                    dbc.FormFloating(
                        [
                            # dbc.Label("Age"),
                            # dbc.Input(
                            #     id="age",
                            #     type="number",
                            #     placeholder="Age",
                            #     className="mb-2",
                            # ),
                            dcc.Dropdown(
                                id="age",
                                options=[
                                    {"label": value, "value": value}
                                    for value in range(21, 101)
                                ],
                                placeholder="Select Age",
                                className="mb-2",
                            ),
                            # dbc.Label("Ballot Order"),
                            # dbc.Input(
                            #     id="ballot",
                            #     type="number",
                            #     placeholder="Ballot Order",
                            #     className="mb-2",
                            # ),
                            dcc.Dropdown(
                                id="ballot",
                                options=[
                                    {"label": value, "value": value}
                                    for value in range(1, 7)
                                ],
                                placeholder="Select Ballot Order",
                                className="mb-2",
                            ),
                            # dbc.Label("Gender"),
                            dcc.Dropdown(
                                id="gender",
                                options=[
                                    {"label": key, "value": value}
                                    for key, value in gender_mapping.items()
                                ],
                                placeholder="Select Gender",
                                className="mb-2",
                            ),
                            # dbc.Label("Party"),
                            dcc.Dropdown(
                                id="party",
                                options=[
                                    {"label": key, "value": value}
                                    for key, value in party_mapping.items()
                                ],
                                placeholder="Select Party",
                                className="mb-2",
                            ),
                            # dbc.Label("Ethnicity"),
                            dcc.Dropdown(
                                id="ethnicity",
                                options=[
                                    {"label": key, "value": value}
                                    for key, value in ethnicity_mapping.items()
                                ],
                                placeholder="Select Ethnicity",
                                className="mb-2",
                            ),
                            # dbc.Label("Parlimen Code"),
                            dcc.Dropdown(
                                id="parlimen",
                                options=[
                                    {"label": code, "value": code}
                                    for code in unique_parlimen_codes
                                ],
                                placeholder="Select a Parlimen Code",
                                className="mb-2",
                            ),
                        ]
                    ),
                    dbc.Button(
                        "Submit",
                        id="submit-val",
                        n_clicks=0,
                        color="primary",
                        className="w-100",
                    ),
                ]
            ),
            className="my-3",
        ),
        html.Hr(),
        html.H2("Predicted Result & GPT-4-Turbo Response", className="mb-3 mt-3"),
        html.Div(id="container-button-basic", className="mb-3"),
        html.Hr(),
        html.H2("Network Graph", className="mb-3 mt-3"),
        html.Iframe(
            src="/assets/network.html", style={"height": "600px", "width": "100%"}
        ),
    ],
    fluid=True,
)


def get_gpt_turbo_response(prompt):
    """
    Sends a prompt to the GPT-4-1106-preview model and retrieves the response.

    Parameters:
    prompt (str): The prompt to send to the model.

    Returns:
    response (dict): The complete response from the GPT model.
    """
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "user", "content": f"{prompt}"},
        ],
    )
    return response


@app.callback(
    Output("container-button-basic", "children"),
    [Input("submit-val", "n_clicks")],
    [
        State("age", "value"),
        State("ballot", "value"),
        State("gender", "value"),
        State("party", "value"),
        State("ethnicity", "value"),
        State("parlimen", "value"),
    ],
)
def update_output(n_clicks, age, ballot_order, gender, party, ethnicity, parlimen):
    """
    Updates the prediction output based on the user inputs from the web form and returns a text response
    with the prediction and reasoning from GPT-4-1106-preview model.

    Parameters:
    n_clicks (int): Number of times the submit button has been clicked.
    age (int): Age of the candidate.
    ballot_order (int): Ballot order of the candidate.
    gender (int): Gender of the candidate, encoded as 1 for male and 0 for female.
    party (int): Party affiliation of the candidate, encoded as an integer.
    ethnicity (int): Ethnicity of the candidate, encoded as an integer.
    parlimen (str): Parlimen code representing the candidate's region.

    Returns:
    str: A formatted string displaying the prediction result and reasoning from GPT-4-Turbo.
    """
    if n_clicks > 0:
        filtered_data = census[census["parlimen"] == parlimen]
        filtered_data = filtered_data.drop(
            ["state", "code_state", "code_parlimen", "year", "parlimen"],
            axis=1,
        )
        filtered_data["ballot_order"] = ballot_order
        filtered_data["age"] = age
        filtered_data["party"] = party
        filtered_data["sex"] = gender
        filtered_data["ethnicity"] = ethnicity

        input_features = filtered_data[X_train.columns.tolist()]
        prediction = rf_classifier.predict(input_features)

        p = list(filter(lambda x: party_mapping[x] == party, party_mapping))[0]
        e = list(
            filter(lambda x: ethnicity_mapping[x] == ethnicity, ethnicity_mapping)
        )[0]

        prompt = f"Provide reasoning for why a candidate from party {p} with these characteristics (age: {age}, gender: {'Male' if gender == 1 else 'Female'}, ethnicity: {e}) in the parlimen region {parlimen} in Malaysia is likely to {'win' if prediction[0] else 'lose'} the election. Please provide some background on the parlimen region and give your explanation in plain text (no formatting)."
        print(prompt)

        # Get GPT-4-Turbo response
        gpt_response = get_gpt_turbo_response(prompt)

        print(gpt_response)

        # Construct the response to be displayed
        result = f"The predicted result is: {'Win' if prediction[0] else 'Lose'}. \n\n Reasoning: {gpt_response.choices[0].message.content}"

        return result


if __name__ == "__main__":
    app.run_server(debug=True)
