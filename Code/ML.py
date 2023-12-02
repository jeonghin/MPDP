from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import pickle
import os
import json

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

# Initialize the Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=123)

# Train the model
rf_classifier.fit(X_train, y_train)

# Make predictions
y_pred = rf_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)


with open("ML.pkl", "wb") as f:
    pickle.dump(rf_classifier, f)
