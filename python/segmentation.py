# ==========================================================
# Marketing Analytics Project
# File Name : segmentation.py
# Purpose   : Rule-Based Customer Segmentation
# ==========================================================

# -----------------------------
# 1. Import Libraries
# -----------------------------
import pandas as pd

# -----------------------------
# 2. Load Cleaned Dataset
# -----------------------------
print("Loading Cleaned Dataset...")

df = pd.read_csv("cleaned_data/marketing_cleaned.csv")

print("Dataset Loaded Successfully!")

# ==========================================================
# RULE 1 : High Income Customer
# Income > 75000
# ==========================================================

df["High_Income"] = df["Income"].apply(
    lambda x: "Yes" if x > 75000 else "No"
)

# ==========================================================
# RULE 2 : Young Customer
# Age < 30
# ==========================================================

df["Young_Customer"] = df["Age"].apply(
    lambda x: "Yes" if x < 30 else "No"
)

# ==========================================================
# RULE 3 : Campaign Responder
# Response == 1
# ==========================================================

df["Campaign_Responder"] = df["Response"].apply(
    lambda x: "Yes" if x == 1 else "No"
)

# ==========================================================
# RULE 4 : High Web Engagement
# NumWebVisitsMonth > 5
# ==========================================================

df["High_Web_Engagement"] = df["NumWebVisitsMonth"].apply(
    lambda x: "Yes" if x > 5 else "No"
)

# ==========================================================
# RULE 5 : Family Customer
# TotalChildren > 0
# ==========================================================

df["Family_Customer"] = df["TotalChildren"].apply(
    lambda x: "Yes" if x > 0 else "No"
)

# ==========================================================
# RULE 6 : High Spender
# TotalSpend > 90th Percentile
# ==========================================================

spend_threshold = df["TotalSpend"].quantile(0.90)

df["High_Spender"] = df["TotalSpend"].apply(
    lambda x: "Yes" if x > spend_threshold else "No"
)

# ==========================================================
# Display Sample Output
# ==========================================================

print("\nSegmentation Preview:\n")

print(
    df[
        [
            "Income",
            "Age",
            "Response",
            "NumWebVisitsMonth",
            "TotalChildren",
            "TotalSpend",
            "High_Income",
            "Young_Customer",
            "Campaign_Responder",
            "High_Web_Engagement",
            "Family_Customer",
            "High_Spender"
        ]
    ].head(10)
)

# ==========================================================
# Segment Summary
# ==========================================================

print("\n========== SEGMENT SUMMARY ==========\n")

print("High Income Customers")
print(df["High_Income"].value_counts())

print("\nYoung Customers")
print(df["Young_Customer"].value_counts())

print("\nCampaign Responders")
print(df["Campaign_Responder"].value_counts())

print("\nHigh Web Engagement")
print(df["High_Web_Engagement"].value_counts())

print("\nFamily Customers")
print(df["Family_Customer"].value_counts())

print("\nHigh Spenders")
print(df["High_Spender"].value_counts())

# ==========================================================
# Save Segmented Dataset
# ==========================================================

df.to_csv(
    "cleaned_data/marketing_segmented.csv",
    index=False
)

print("\n===================================")
print("Segmentation Completed Successfully!")
print("File Saved : cleaned_data/marketing_segmented.csv")
print("===================================")