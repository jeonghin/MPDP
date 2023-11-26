import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np


candidate = pd.read_csv("Data/candidates_ge15.csv")
candidate.fillna(candidate.age.mean(), inplace=True)
census = pd.read_csv("Data/census_parlimen.csv")
census.fillna(census.sme_small.mean(), inplace=True)
# results = pd.read_csv("Data/results_parlimen_ge15.csv")

merged_df = candidate.merge(census, on=["state", "parlimen"], how="left")
# merged_df = merged_df.merge(results, on=["state", "parlimen"], how="left")

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

merged_df["sex"] = merged_df["sex"].map(gender_mapping)
merged_df["ethnicity"] = merged_df["ethnicity"].map(ethnicity_mapping)
merged_df["party"] = merged_df["party"].map(party_mapping)

# Training the RandomForestClassifier
target_column = "result"

# label_encoder = LabelEncoder()
# categorical_columns = merged_df.select_dtypes(include=["object"]).columns
# for column in categorical_columns:
#     merged_df[column] = label_encoder.fit_transform(merged_df[column])

# Define features (X) and target (y)
X = merged_df.drop(target_column, axis=1)
y = merged_df[target_column]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123
)

# Initialize the Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=123)

# Train the model
rf_classifier.fit(X_train, y_train)

# Make predictions
y_pred = rf_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

unique_parlimen_codes = candidate["parlimen"].unique()

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Input(id="age", type="number", placeholder="Age"),
        dcc.Input(id="ballot", type="number", placeholder="Ballot Order"),
        dcc.Dropdown(
            id="gender",
            options=[
                {"label": key, "value": value} for key, value in gender_mapping.items()
            ],
            placeholder="Select the gender",
        ),
        dcc.Dropdown(
            id="party",
            options=[
                {"label": key, "value": value} for key, value in party_mapping.items()
            ],
            placeholder="Select the party",
        ),
        dcc.Dropdown(
            id="ethnicity",
            options=[
                {"label": key, "value": value}
                for key, value in ethnicity_mapping.items()
            ],
            placeholder="Select the ethnicity",
        ),
        dcc.Dropdown(
            id="parlimen",
            options=[{"label": code, "value": code} for code in unique_parlimen_codes],
            placeholder="Select a Parlimen Code",
        ),
        html.Button("Submit", id="submit-val", n_clicks=0),
        html.Div(id="container-button-basic"),
    ]
)


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

        # Replace the feature values with the ones received from the user input
        # input_features = pd.DataFrame([[age, party]], columns=["age", "party"])
        # prediction = rf_classifier.predict(input_features)

        return f"The predicted result is: {'Win' if prediction[0] else 'Lose'}"


if __name__ == "__main__":
    app.run_server(debug=True)
