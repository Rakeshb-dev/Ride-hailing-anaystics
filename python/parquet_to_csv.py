import pandas as pd

# Load BI-ready parquet
gold = pd.read_parquet("data/gold/gold_ride_demand_bi.parquet")

# Save as CSV for Tableau
gold.to_csv(
    "data/gold/gold_ride_demand_bi.csv",
    index=False
)

print("CSV file created for Tableau")
print(gold.head())
