# Afficionado Coffee Roasters — Sales Performance Analysis

## 📊 Project Overview

This project analyzes sales performance for Afficionado Coffee Roasters
using Python and Power BI.

The objective is to identify revenue trends, store performance,
product category performance, and hourly demand patterns to support
data-driven business decisions.

---

## 🎯 Business Objectives

- Analyze overall sales performance
- Identify the highest-performing stores
- Identify top revenue-generating product categories
- Analyze hourly customer demand
- Compare Morning, Afternoon, and Evening performance
- Develop actionable business recommendations
- Build an interactive Power BI dashboard

---

## 🗂️ Dataset

The dataset contains coffee shop transaction-level sales information.

### Key Columns

- transaction_id
- year
- transaction_time
- transaction_qty
- store_id
- store_location
- product_id
- unit_price
- product_category
- product_type
- product_detail

The dataset contains **149,116 transactions** across **3 stores** and
**80 products**.

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- OpenPyXL
- Jupyter Notebook
- Power BI
- DAX
- VS Code
- Git / GitHub

---

## 🔧 Data Preparation

The dataset was checked for:

- Missing values
- Duplicate records
- Data types
- Invalid values
- Required columns

The dataset contained:

- **0 missing values**
- **0 duplicate rows**

---

## ⚙️ Feature Engineering

The following business features were created:

### Revenue

Revenue was calculated using:

`Revenue = Transaction Quantity × Unit Price`

### Hour

Transaction time was converted into an hourly feature.

### Time Bucket

Transactions were grouped into:

- Morning
- Afternoon
- Evening

---

## 📈 Key Performance Indicators

| KPI | Value |
|---|---:|
| Total Revenue | $698,812.33 |
| Total Transactions | 149,116 |
| Total Units Sold | 214,470 |
| Average Transaction Value | $4.69 |
| Total Stores | 3 |
| Total Products | 80 |
| Product Categories | 9 |

---

## 🔍 Key Business Insights

### ☕ Coffee is the leading category

Coffee generated **$269,952.45**, making it the highest-revenue
product category.

### 🌅 Morning is the strongest period

Morning generated **$388,288.67**, representing approximately
**55.6% of total revenue**.

### ⏰ 10 AM is the peak revenue hour

10 AM generated the highest hourly revenue at approximately
**$88,673.39**.

### 🏪 Store performance is relatively balanced

Hell's Kitchen generated the highest revenue at **$236,511.17**,
while the three stores remained relatively close in overall revenue.

### ☕ Core beverages dominate revenue

Coffee and Tea together contribute approximately **66.7% of total
revenue**.

---

## 💡 Business Recommendations

1. Evaluate staffing and inventory requirements during the morning
   peak period.

2. Maintain strong availability of Coffee and Tea products because
   they represent the majority of revenue.

3. Investigate lower evening demand to identify opportunities for
   improving evening performance.

4. Compare product-level performance across stores to identify
   location-specific opportunities.

---

## 📊 Power BI Dashboard

The interactive Power BI dashboard provides:

- KPI cards
- Revenue by Store
- Revenue by Product Category
- Hourly Revenue Trend
- Revenue by Time of Day
- Store Location slicer
- Product Category slicer
- Time Bucket slicer

The dashboard is designed to provide an interactive view of business
performance.

---

## 📁 Project Structure

```text
Project DA/
│
├── data/
│   └── Afficionado Coffee Roasters.xlsx
│
├── src/
│   ├── data_loader.py
│   ├── feature_engineering.py
│   ├── analysis.py
│   └── visualization.py
│
├── outputs/
│   ├── charts/
│   ├── reports/
│   │   └── business_insights.md
│   └── processed_coffee_data.csv
│
├── powerbi/
│   └── Afficionado_Coffee_Dashboard.pbix
│
├── requirements.txt
├── .gitignore
└── README.md