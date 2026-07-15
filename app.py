import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
# PAGE SETTINGS
# ==========================================================

st.set_page_config(
    page_title="Marketing Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# LOAD DATA
# ==========================================================
df = pd.read_csv("cleaned_data/marketing_segmented.csv")
# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("🔍 Filters")

country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + sorted(df["Country"].unique().tolist())
)

education = st.sidebar.selectbox(
    "Select Education",
    ["All"] + sorted(df["Education"].unique().tolist())
)

marital = st.sidebar.selectbox(
    "Select Marital Status",
    ["All"] + sorted(df["Marital_Status"].unique().tolist())
)

filtered_df = df.copy()

if country != "All":
    filtered_df = filtered_df[filtered_df["Country"] == country]

if education != "All":
    filtered_df = filtered_df[filtered_df["Education"] == education]

if marital != "All":
    filtered_df = filtered_df[filtered_df["Marital_Status"] == marital]

# ==========================================================
# TITLE
# ==========================================================

st.title("📊 Marketing Analytics Dashboard")

st.markdown(
"""
### Customer Segmentation & Campaign Performance Analysis

This dashboard analyzes customer demographics, spending behaviour,
campaign performance and purchase channels.
"""
)

st.divider()

# ==========================================================
# KPI CARDS
# ==========================================================

st.subheader("📌 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

total_customers = len(filtered_df)
average_income = filtered_df["Income"].mean()
average_spending = filtered_df["TotalSpend"].mean()
response_rate = filtered_df["Response"].mean() * 100

col1.metric("👥 Customers", f"{total_customers:,}")

col2.metric("💰 Avg Income", f"₹{average_income:,.0f}")

col3.metric("🛒 Avg Spending", f"₹{average_spending:,.0f}")

col4.metric("📈 Response Rate", f"{response_rate:.2f}%")

st.divider()

# ==========================================================
# CHARTS
# ==========================================================

col1, col2 = st.columns(2)

# ---------------- Age Distribution ----------------

with col1:

    st.subheader("Age Distribution")

    fig, ax = plt.subplots(figsize=(6,4))

    ax.hist(filtered_df["Age"], bins=20)

    ax.set_xlabel("Age")

    ax.set_ylabel("Customers")

    st.pyplot(fig)

# ---------------- Income Distribution ----------------

with col2:

    st.subheader("Income Distribution")

    fig, ax = plt.subplots(figsize=(6,4))

    ax.hist(filtered_df["Income"], bins=20)

    ax.set_xlabel("Income")

    ax.set_ylabel("Customers")

    st.pyplot(fig)

# ==========================================================

col3, col4 = st.columns(2)

# ---------------- Product Spending ----------------

with col3:

    st.subheader("Product Category Spending")

    product_names = [
        "Wines",
        "Fruits",
        "Meat",
        "Fish",
        "Sweets",
        "Gold"
    ]

    spending = [
        filtered_df["MntWines"].sum(),
        filtered_df["MntFruits"].sum(),
        filtered_df["MntMeatProducts"].sum(),
        filtered_df["MntFishProducts"].sum(),
        filtered_df["MntSweetProducts"].sum(),
        filtered_df["MntGoldProds"].sum()
    ]

    fig, ax = plt.subplots(figsize=(6,4))

    ax.bar(product_names, spending)

    ax.set_ylabel("Total Spending")

    plt.xticks(rotation=20)

    st.pyplot(fig)

# ---------------- Campaign Response ----------------

with col4:

    st.subheader("Campaign Response")

    response = filtered_df["Response"].value_counts()

    fig, ax = plt.subplots(figsize=(6,4))

    ax.pie(
        response,
        labels=["No", "Yes"],
        autopct="%1.1f%%",
        startangle=90
    )

    ax.axis("equal")

    st.pyplot(fig)

st.divider()

# ==========================================================
# SEGMENT SUMMARY
# ==========================================================

st.subheader("📊 Customer Segments")

segment1, segment2, segment3 = st.columns(3)

high_income = (filtered_df["High_Income"] == "Yes").sum()
high_spender = (filtered_df["High_Spender"] == "Yes").sum()
campaign = (filtered_df["Campaign_Responder"] == "Yes").sum()

segment1.success(f"High Income Customers : {high_income}")

segment2.success(f"High Spenders : {high_spender}")

segment3.success(f"Campaign Responders : {campaign}")

st.divider()

# ==========================================================
# DATASET
# ==========================================================

st.subheader("📄 Customer Dataset")

st.dataframe(filtered_df)

st.divider()

# ==========================================================
# RECOMMENDATIONS
# ==========================================================

st.subheader("💡 Business Recommendations")

st.markdown("""
1. Target **high-income customers** with premium products.

2. Focus future campaigns on **previous campaign responders**.

3. Promote products through **web channels** for highly engaged customers.

4. Offer **family discount campaigns** for customers with children.

5. Increase marketing investment in **high-spending customer segments**.
""")

st.divider()

st.caption("Marketing Analytics Dashboard | Python • Pandas • Streamlit • MySQL")