# scripts/customer_segmentation.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Paths
data_file = "data/cleaned_data.csv"
output_file = "data/customer_segments.csv"
plots_dir = "plots"
if not os.path.exists(plots_dir):
    os.makedirs(plots_dir)

# Load the cleaned data
df = pd.read_csv(data_file)

# Creating customer segments based on tenure
df['Tenure Group'] = pd.cut(df['tenure'], bins=[0, 12, 24, 48, 72], labels=['0-12', '13-24', '25-48', '49-72'])

# Creating customer segments based on Monthly Charges
df['Monthly Charges Group'] = pd.cut(df['MonthlyCharges'], bins=[0, 30, 60, 90, 120], labels=['Low', 'Medium', 'High', 'Very High'])

# Summarizing the customer segments
segment_summary = df.groupby(['Tenure Group', 'Monthly Charges Group', 'Churn'], observed=False).size().unstack().fillna(0)


# Save the segmentation summary
segment_summary.to_csv(output_file)

# Plotting the segmentation distribution
plt.figure(figsize=(14, 8))
sns.heatmap(segment_summary, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("Customer Segmentation (Tenure vs Monthly Charges) with Churn Status")
plt.savefig(os.path.join(plots_dir, "customer_segmentation_heatmap.png"))
plt.show()

print("\nCustomer segmentation completed. Summary saved to 'data/customer_segments.csv'.")
