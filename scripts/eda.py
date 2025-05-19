# scripts/eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Paths
data_file = "data/cleaned_data.csv"
plots_dir = "plots"
if not os.path.exists(plots_dir):
    os.makedirs(plots_dir)

# Load the cleaned data
df = pd.read_csv(data_file)

# Basic data overview
print("\nBasic Data Info:")
print(df.info())

print("\nData Summary:")
print(df.describe())

print("\nChurn Distribution:")
print(df['Churn'].value_counts(normalize=True))

# Plot churn distribution
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Churn', hue='Churn', palette='viridis', dodge=False, legend=False)
plt.title("Customer Churn Distribution")
plt.savefig(os.path.join(plots_dir, "churn_distribution.png"))
plt.show()

# Correlation heatmap for numerical features
# Correlation heatmap for numerical features
numeric_df = df[['tenure', 'MonthlyCharges', 'TotalCharges']]
plt.figure(figsize=(12,8))
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap (Numerical Features)")
plt.title("Correlation Heatmap (Numerical Features)")
plt.savefig(os.path.join(plots_dir, "correlation_heatmap.png"))
plt.show()

# Save the correlation matrix to CSV
numeric_df.corr().to_csv("data/correlation_matrix.csv")


print("\nEDA completed. Plots saved to 'plots/' directory.")
