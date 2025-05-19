# Telco Customer Churn Analysis

## 📊 Project Overview

This project focuses on analyzing customer churn behavior in the telecommunications industry using the Telco Customer Churn dataset. The goal is to gain insights into customer behavior, identify key churn drivers, and create actionable customer segments for better retention strategies. This analysis includes data cleaning, exploratory data analysis (EDA), customer segmentation, and Excel-based financial analysis.

## 🗂️ Project Structure

```
Telco_Customer_Churn_Analysis/
├── data/
│   ├── telco_customer_churn.csv        # Raw data file
│   ├── cleaned_data.csv                # Cleaned data file
│   ├── customer_segments.csv           # Customer segmentation summary
│   └── correlation_matrix.csv          # Correlation matrix for numerical features
├── scripts/
│   ├── data_cleaning.py                # Data cleaning script
│   ├── eda.py                          # Exploratory data analysis script
│   ├── customer_segmentation.py        # Customer segmentation script
│ 
├── notebooks/
│   └── churn_analysis_master.ipynb     # Jupyter notebook for full project
├── plots/
│   ├── churn_distribution.png          # Churn distribution plot
│   ├── correlation_heatmap.png         # Correlation heatmap for numerical features
│   └── customer_segmentation_heatmap.png # Customer segmentation heatmap
└── 
```

## 🚀 Key Features

* **Data Cleaning:** Removing irrelevant columns, handling missing values, and data type corrections.
* **Exploratory Data Analysis (EDA):** Generating visual insights to understand churn behavior.
* **Customer Segmentation:** Grouping customers based on tenure, monthly charges, and churn status.
* **Data Export:** Saving key insights and segmentation results to CSV files.

## 🔧 Setup and Installation

1. Clone this repository:

```
git clone https://github.com/DevtronixAI42/Telco_Customer_Churn_Analysis.git
cd Telco_Customer_Churn_Analysis
```

2. Install the required Python packages:

```
pip install pandas matplotlib seaborn
```

3. Ensure the data files are placed in the `data/` directory.

## 📂 Scripts

* **data\_cleaning.py:** Cleans the raw data for analysis.
* **eda.py:** Performs exploratory data analysis and visualizations.
* **customer\_segmentation.py:** Creates customer segments based on tenure and monthly charges.

## 📊 Outputs

* Cleaned data file (`data/cleaned_data.csv`)
* Customer segmentation summary (`data/customer_segments.csv`)
* Correlation matrix (`data/correlation_matrix.csv`)
* EDA and segmentation visualizations (`plots/`)

## 📋 Future Improvements

* Add more advanced segmentation techniques (e.g., RFM analysis).
* Integrate Power BI or Tableau for interactive dashboards.
* Explore machine learning models for churn prediction.

## 🤝 Contributing

Feel free to fork this project, make changes, and submit pull requests to improve the analysis.

## 📄 License

This project is open-source and available under the MIT License.

