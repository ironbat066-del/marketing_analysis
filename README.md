# 📊 Marketing Analytics Dashboard

## 📌 Project Overview

This project analyzes customer marketing data to identify customer behavior, spending patterns, campaign performance, and customer segments. The project uses Python for data preprocessing, MySQL for database analysis, and Streamlit for an interactive dashboard.

---

## 🎯 Objectives

- Clean and preprocess marketing data
- Perform Exploratory Data Analysis (EDA)
- Create rule-based customer segments
- Store data in MySQL
- Perform SQL analysis
- Build an interactive Streamlit dashboard
- Generate business recommendations

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- MySQL
- Streamlit

---

## 📂 Project Structure

```
Marketing_Analytics_Project/
│
├── Dashboard/
│   └── app.py
│
├── python/
│   ├── cleaning.py
│   ├── eda.py
│   └── segmentation.py
│
├── data/
│   ├── marketing_campaign_data.csv
│   └── marketing_data_dictionary.csv
│
├── cleaned_data/
│   ├── marketing_cleaned.csv
│   └── marketing_segmented.csv
│
├── sql/
│   └── marketing_queries.sql
│
├── images/
│   ├── age_distribution.png
│   ├── income_distribution.png
│   ├── product_spending.png
│   ├── campaign_response.png
│
├── requirements.txt
└── README.md
```

---

## 📊 Features

### Data Cleaning
- Removed duplicate records
- Converted date columns
- Created new features:
  - Age
  - Total Children
  - Total Spend
  - Total Purchases
  - Total Accepted Campaigns

### Exploratory Data Analysis
- Age Distribution
- Income Distribution
- Spending Analysis
- Country Analysis
- Education Analysis
- Marital Status Analysis
- Product Spending
- Purchase Channel Analysis
- Campaign Response
- Correlation Heatmap
- Total Purchases Distribution

### Customer Segmentation

Rule-based segmentation includes:

- High Income Customers
- Young Customers
- Campaign Responders
- High Web Engagement
- Family Customers
- High Spenders

### SQL Analysis

The project includes SQL queries for:

- Customer KPIs
- Spending Analysis
- Campaign Analysis
- Customer Segmentation
- Product Analysis
- Purchase Channel Analysis

### Interactive Dashboard

The Streamlit dashboard provides:

- KPI Cards
- Interactive Filters
- Charts
- Customer Segment Summary
- Dataset Preview
- Business Recommendations

---

## 💡 Business Recommendations

- Target high-income customers with premium products.
- Focus future campaigns on previous campaign responders.
- Increase online marketing for highly engaged customers.
- Offer family discounts for customers with children.
- Promote premium products to high-spending customers.

---

## ▶️ How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Dashboard

```bash
python -m streamlit run Dashboard/app.py
```

---

## 📷 Dashboard Preview

Add screenshots of your dashboard in the **images** folder and include them here.

Example:

```
images/dashboard_home.png
images/dashboard_filters.png
```

---

## 👨‍💻 Author

Marketing Analytics Dashboard Project

Developed using Python, MySQL, and Streamlit.