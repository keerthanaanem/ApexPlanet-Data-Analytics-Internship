# TASK 1: DATA IMMERSION & WRANGLING
 

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------
# 1. Load RAW Dataset
# ------------------------------------------
df = pd.read_excel("/content/Raw_Dataset.xlsx")

print("Dataset Shape:", df.shape)
print("\nDataset Info:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

# ------------------------------------------
# 2. Data Quality Assessment
# ------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:", df.duplicated().sum())

# ------------------------------------------
# 3. Data Cleaning
# ------------------------------------------

# Remove duplicates
df_cleaned = df.drop_duplicates()

# Handle missing values (example: drop rows with missing values)
df_cleaned = df_cleaned.dropna()

# ------------------------------------------
# 4. Data Transformation
# ------------------------------------------

# Create Total Sales column
df_cleaned["Total_Sales"] = df_cleaned["Quantity"] * df_cleaned["Price"]

print("\nCleaned Dataset Shape:", df_cleaned.shape)

# ------------------------------------------
# 5. Save CLEANED Dataset
# ------------------------------------------

df_cleaned.to_excel("/content/Cleaned_Dataset.xlsx", index=False)

print("Cleaned dataset saved successfully!")
