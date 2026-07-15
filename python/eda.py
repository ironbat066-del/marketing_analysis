# ==========================================================
# Marketing Analytics Project
# File Name : eda.py
# Purpose   : Exploratory Data Analysis (EDA)
# ==========================================================

# -----------------------------
# Import Libraries
# -----------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Dataset
# -----------------------------
print("Loading Cleaned Dataset...")

df = pd.read_csv("cleaned_data/marketing_cleaned.csv")

print("Dataset Loaded Successfully!")

# -----------------------------
# Graph Style
# -----------------------------
sns.set_style("whitegrid")

# ==========================================================
# 1. Age Distribution
# ==========================================================

plt.figure(figsize=(10,6))
sns.histplot(df["Age"], bins=20, kde=True, color="steelblue")
plt.title("Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("images/age_distribution.png", dpi=300)
plt.show()

# ==========================================================
# 2. Income Distribution
# ==========================================================

plt.figure(figsize=(10,6))
sns.histplot(df["Income"], bins=30, kde=True, color="green")
plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("images/income_distribution.png", dpi=300)
plt.show()

# ==========================================================
# 3. Education Distribution
# ==========================================================

plt.figure(figsize=(10,6))
sns.countplot(data=df, x="Education", order=df["Education"].value_counts().index)
plt.title("Education Distribution")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("images/education_distribution.png", dpi=300)
plt.show()

# ==========================================================
# 4. Marital Status
# ==========================================================

plt.figure(figsize=(10,6))
sns.countplot(data=df, x="Marital_Status", order=df["Marital_Status"].value_counts().index)
plt.title("Marital Status Distribution")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("images/marital_status_distribution.png", dpi=300)
plt.show()

# ==========================================================
# 5. Country Distribution
# ==========================================================

plt.figure(figsize=(12,6))
sns.countplot(data=df, x="Country", order=df["Country"].value_counts().index)
plt.title("Customers by Country")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/country_distribution.png", dpi=300)
plt.show()

# ==========================================================
# 6. Product Spending
# ==========================================================

product_spend = df[
[
"MntWines",
"MntFruits",
"MntMeatProducts",
"MntFishProducts",
"MntSweetProducts",
"MntGoldProds"
]
].sum()

plt.figure(figsize=(10,6))
product_spend.plot(kind="bar")
plt.title("Total Spending by Product Category")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("images/product_spending.png", dpi=300)
plt.show()

# ==========================================================
# 7. Purchase Channels
# ==========================================================

channel = df[
[
"NumWebPurchases",
"NumCatalogPurchases",
"NumStorePurchases"
]
].sum()

plt.figure(figsize=(8,6))
channel.plot(kind="bar")
plt.title("Purchases by Channel")
plt.ylabel("Number of Purchases")
plt.tight_layout()
plt.savefig("images/purchase_channels.png", dpi=300)
plt.show()

# ==========================================================
# 8. Campaign Acceptance
# ==========================================================

campaigns = df[
[
"AcceptedCmp1",
"AcceptedCmp2",
"AcceptedCmp3",
"AcceptedCmp4",
"AcceptedCmp5",
"Response"
]
].sum()

plt.figure(figsize=(8,6))
campaigns.plot(kind="bar")
plt.title("Campaign Acceptance")
plt.ylabel("Accepted Customers")
plt.tight_layout()
plt.savefig("images/campaign_response.png", dpi=300)
plt.show()

# ==========================================================
# 9. Income vs Total Spend
# ==========================================================

plt.figure(figsize=(10,6))
sns.scatterplot(
data=df,
x="Income",
y="TotalSpend"
)

plt.title("Income vs Total Spend")
plt.tight_layout()
plt.savefig("images/income_vs_spending.png", dpi=300)
plt.show()

# ==========================================================
# 10. Age vs Total Spend
# ==========================================================

plt.figure(figsize=(10,6))
sns.scatterplot(
data=df,
x="Age",
y="TotalSpend"
)

plt.title("Age vs Total Spend")
plt.tight_layout()
plt.savefig("images/age_vs_spending.png", dpi=300)
plt.show()

# ==========================================================
# 11. Correlation Heatmap
# ==========================================================

plt.figure(figsize=(14,10))

sns.heatmap(
df.select_dtypes(include="number").corr(),
annot=True,
fmt=".2f",
cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("images/correlation_heatmap.png", dpi=300)
plt.show()

print("\n====================================")
print("EDA COMPLETED SUCCESSFULLY")
print("All Charts Saved in images Folder")
print("====================================")