import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# Project path
BASE_DIR = Path(__file__).resolve().parent.parent

# Load processed data
file_path = BASE_DIR / "outputs" / "processed_coffee_data.csv"
df = pd.read_csv(file_path)


# Create output folder
chart_path = BASE_DIR / "outputs" / "charts"
chart_path.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# 1. REVENUE BY STORE
# --------------------------------------------------

store_revenue = (
    df.groupby("store_location")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
store_revenue.plot(kind="bar")

plt.title("Revenue by Store")
plt.xlabel("Store Location")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(chart_path / "revenue_by_store.png")
plt.close()


# --------------------------------------------------
# 2. REVENUE BY PRODUCT CATEGORY
# --------------------------------------------------

category_revenue = (
    df.groupby("product_category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
category_revenue.plot(kind="bar")

plt.title("Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(chart_path / "revenue_by_category.png")
plt.close()


# --------------------------------------------------
# 3. HOURLY REVENUE
# --------------------------------------------------

hourly_revenue = (
    df.groupby("hour")["revenue"]
    .sum()
)

plt.figure(figsize=(10, 6))
hourly_revenue.plot(kind="line", marker="o")

plt.title("Hourly Revenue Trend")
plt.xlabel("Hour")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.tight_layout()

plt.savefig(chart_path / "hourly_revenue.png")
plt.close()


# --------------------------------------------------
# 4. REVENUE BY TIME BUCKET
# --------------------------------------------------

time_revenue = (
    df.groupby("time_bucket")["revenue"]
    .sum()
    .reindex(["Morning", "Afternoon", "Evening"])
)

plt.figure(figsize=(8, 6))
time_revenue.plot(kind="bar")

plt.title("Revenue by Time of Day")
plt.xlabel("Time Bucket")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(chart_path / "revenue_by_time_bucket.png")
plt.close()


print("Visualization completed successfully!")
print(f"Charts saved to: {chart_path}")