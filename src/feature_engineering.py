import pandas as pd
from pathlib import Path


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "Afficionado Coffee Roasters.xlsx"


# Load dataset
df = pd.read_excel(file_path)


# Convert transaction time
df["transaction_time"] = pd.to_datetime(
    df["transaction_time"],
    format="%H:%M:%S"
)


# Revenue
df["revenue"] = df["transaction_qty"] * df["unit_price"]


# Time features
df["hour"] = df["transaction_time"].dt.hour


# Create a date using the year and transaction sequence context
# For now, use the available year and transaction time for time-based analysis
#df["day_of_week"] = df["transaction_time"].dt.day_name()


# Time buckets
def get_time_bucket(hour):
    if 6 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"


df["time_bucket"] = df["hour"].apply(get_time_bucket)


# Displaying results
print("Feature Engineering Completed!")
print("\nNew Columns:")
print(df.columns.tolist())

print("\nSample Data:")
print(
    df[
        [
            "transaction_qty",
            "unit_price",
            "revenue",
            "hour",
            #"day_of_week",
            "time_bucket"
        ]
    ].head()
)
# Saving processed dataset
output_path = BASE_DIR / "outputs" / "processed_coffee_data.csv"
df.to_csv(output_path, index=False)
print(f"\nProcessed dataset saved to: {output_path}")