# ==========================================================
# Marketing Analytics Project
# File Name : cleaning.py
# Purpose   : Data Cleaning & Feature Engineering
# Author    : Your Name
# ==========================================================

# -----------------------------
# 1. Import Required Libraries
# -----------------------------
from concurrent.interpreters import Interpreter

import pandas as pd
import numpy as np

# -----------------------------
# 2. Load Dataset
# -----------------------------
print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv("data/marketing_campaign_data.csv")

print("✅ Dataset Loaded Successfully!")

# -----------------------------
# 3. Data Inspection
# -----------------------------
print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== DATASET INFORMATION ==========")
df.info()

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

# -----------------------------
# 4. Data Cleaning
# -----------------------------
print("\nCleaning Data...")

# Convert customer enrollment date to datetime format
df["Dt_Customer"] = pd.to_datetime(
    df["Dt_Customer"],
    errors="coerce"
)

print("✅ Date column converted successfully.")

# -----------------------------
# 5. Feature Engineering
# -----------------------------
print("\nCreating New Features...")

current_year = 2026

# Customer Age
df["Age"] = current_year - df["Year_Birth"]

# Total Children
df["TotalChildren"] = df["Kidhome"] + df["Teenhome"]

# Total Spending
df["TotalSpend"] = (
    df["MntWines"]
    + df["MntFruits"]
    + df["MntMeatProducts"]
    + df["MntFishProducts"]
    + df["MntSweetProducts"]
    + df["MntGoldProds"]
)

# Total Purchases
df["TotalPurchases"] = (
    df["NumDealsPurchases"]
    + df["NumWebPurchases"]
    + df["NumCatalogPurchases"]
    + df["NumStorePurchases"]
)

# Total Accepted Campaigns
df["TotalAcceptedCampaigns"] = (
    df["AcceptedCmp1"]
    + df["AcceptedCmp2"]
    + df["AcceptedCmp3"]
    + df["AcceptedCmp4"]
    + df["AcceptedCmp5"]
)

print("✅ New Features Created Successfully!")

# -----------------------------
# 6. Display Newly Created Columns
# -----------------------------
print("\n========== NEW FEATURES ==========")

print(
    df[
        [
            "Age",
            "TotalChildren",
            "TotalSpend",
            "TotalPurchases",
            "TotalAcceptedCampaigns"
        ]
    ].head()
)

# -----------------------------
# 7. Save Cleaned Dataset
# -----------------------------
print("\nSaving Cleaned Dataset...")

df.to_csv(
    "cleaned_data/marketing_cleaned.csv",
    index=False
)

print("✅ Cleaned dataset saved successfully!")

# -----------------------------
# 8. Project Summary
# -----------------------------
print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("=" * 60)
print(f"Total Records            : {len(df)}")
print(f"Total Columns            : {len(df.columns)}")
print("New Columns Added        :")
print("   • Age")
print("   • TotalChildren")
print("   • TotalSpend")
print("   • TotalPurchases")
print("   • TotalAcceptedCampaigns")
print("\nOutput File:")
print("cleaned_data/marketing_cleaned.csv")
print("=" * 60)