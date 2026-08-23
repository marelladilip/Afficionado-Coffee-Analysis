from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "Afficionado Coffee Roasters.xlsx"
df = pd.read_excel(file_path)

print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())