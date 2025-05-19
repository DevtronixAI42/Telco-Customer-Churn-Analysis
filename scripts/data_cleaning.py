# scripts/data_cleaning.py

import pandas as pd
import os

# Paths
input_file = "data/telco_customer_churn.csv"
output_file = "data/cleaned_data.csv"

# Load the raw data
df = pd.read_csv(input_file)

# Inspect the data
print("\nInitial Data Overview:")
print(df.info())
print("\nMissing Values:")
print(df.isna().sum())

# Drop customerID as it's just an identifier
df.drop(columns=['customerID'], inplace=True)

# Handle missing values in TotalCharges (convert to numeric, drop NaNs)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)

# Convert SeniorCitizen from 0/1 to 'No'/'Yes'
df['SeniorCitizen'] = df['SeniorCitizen'].replace({1: 'Yes', 0: 'No'})

# Save cleaned data
df.to_csv(output_file, index=False)

print(f"\nData cleaned and saved to {output_file}.")
print("\nCleaned Data Overview:")
print(df.info())
