import pandas as pd
from pathlib import Path


# Project path
BASE_DIR = Path(__file__).resolve().parent.parent

# Load processed data
file_path = BASE_DIR / "outputs" / "processed_coffee_data.csv"

df = pd.read_csv(file_path)


# -----------------------------
# BUSINESS KPI ANALYSIS
# -----------------------------

total_revenue = df["revenue"].sum()
total_transactions = df["transaction_id"].nunique()
total_units_sold = df["transaction_qty"].sum()
average_transaction_value = total_revenue / total_transactions

total_stores = df["store_id"].nunique()
total_products = df["product_id"].nunique()
total_categories = df["product_category"].nunique()


print("=" * 50)
print("AFFICIONADO COFFEE ROASTERS - BUSINESS KPIs")
print("=" * 50)

print(f"Total Revenue          : ${total_revenue:,.2f}")
print(f"Total Transactions     : {total_transactions:,}")
print(f"Total Units Sold       : {total_units_sold:,}")
print(f"Average Transaction    : ${average_transaction_value:,.2f}")
print(f"Total Stores           : {total_stores}")
print(f"Total Products         : {total_products}")
print(f"Product Categories     : {total_categories}")


# -----------------------------
# STORE PERFORMANCE
# -----------------------------

store_performance = (
    df.groupby(["store_id", "store_location"])
    .agg(
        revenue=("revenue", "sum"),
        units_sold=("transaction_qty", "sum"),
        transactions=("transaction_id", "nunique")
    )
    .sort_values("revenue", ascending=False)
)

print("\n" + "=" * 50)
print("STORE PERFORMANCE")
print("=" * 50)

print(store_performance)


# -----------------------------
# CATEGORY PERFORMANCE
# -----------------------------

category_performance = (
    df.groupby("product_category")
    .agg(
        revenue=("revenue", "sum"),
        units_sold=("transaction_qty", "sum"),
        transactions=("transaction_id", "nunique")
    )
    .sort_values("revenue", ascending=False)
)

print("\n" + "=" * 50)
print("CATEGORY PERFORMANCE")
print("=" * 50)

print(category_performance)


# -----------------------------
# HOURLY DEMAND
# -----------------------------

hourly_demand = (
    df.groupby("hour")
    .agg(
        revenue=("revenue", "sum"),
        transactions=("transaction_id", "nunique"),
        units_sold=("transaction_qty", "sum")
    )
    .sort_index()
)

print("\n" + "=" * 50)
print("HOURLY DEMAND")
print("=" * 50)

print(hourly_demand)


# -----------------------------
# TIME BUCKET PERFORMANCE
# -----------------------------

time_bucket_performance = (
    df.groupby("time_bucket")
    .agg(
        revenue=("revenue", "sum"),
        transactions=("transaction_id", "nunique"),
        units_sold=("transaction_qty", "sum")
    )
    .sort_values("revenue", ascending=False)
)

print("\n" + "=" * 50)
print("TIME BUCKET PERFORMANCE")
print("=" * 50)

print(time_bucket_performance)