# ==========================================
# TASK 2: EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------
# 1. Load CLEANED Dataset
# ------------------------------------------
df = pd.read_csv("/content/cleaned_data.csv")

print("Dataset Shape:", df.shape)
print("\nDataset Info:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

# ------------------------------------------
# 2. Basic Data Understanding
# ------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

# ------------------------------------------
# 3. Feature Engineering
# ------------------------------------------

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Extract Month and Year
df["Month"] = df["InvoiceDate"].dt.month
df["Year"] = df["InvoiceDate"].dt.year

# Revenue column already exists (Total_Sales)
print("\nNew Columns Added: Month, Year")

# ------------------------------------------
# 4. Univariate Analysis
# ------------------------------------------

# 4.1 Top 10 Countries by number of orders
plt.figure()
df["Country"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Countries by Orders")
plt.xlabel("Country")
plt.ylabel("Number of Orders")
plt.show()

# 4.2 Quantity distribution
plt.figure()
df["Quantity"].hist(bins=30)
plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.show()

# ------------------------------------------
# 5. Multivariate Analysis
# ------------------------------------------

# 5.1 Monthly Revenue Trend
monthly_revenue = df.groupby("Month")["Total_Sales"].sum()

plt.figure()
monthly_revenue.plot(kind="line", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.show()

# 5.2 Top 10 Products by Revenue
top_products = df.groupby("Description")["Total_Sales"].sum().sort_values(ascending=False).head(10)

plt.figure()
top_products.plot(kind="bar")
plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

# 5.3 Quantity vs Revenue
plt.figure()
sns.scatterplot(x="Quantity", y="Total_Sales", data=df)
plt.title("Quantity vs Revenue")
plt.show()

# ------------------------------------------
# 6. Business Insights
# ------------------------------------------

# Top 5 countries by revenue
top_countries = df.groupby("Country")["Total_Sales"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Countries by Revenue:")
print(top_countries)

# Average order value
avg_order_value = df["Total_Sales"].mean()
print("\nAverage Order Value:", avg_order_value)

# ------------------------------------------
# 7. Save EDA Results
# ------------------------------------------

# Save summary table
summary_table = df.groupby("Country")["Total_Sales"].sum().reset_index()
summary_table.to_csv("/content/eda_summary_by_country.csv", index=False)

print("\n✅ Task-2 EDA Completed Successfully!")
print("EDA summary saved as: /content/eda_summary_by_country.csv")
