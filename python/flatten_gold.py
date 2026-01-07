import pandas as pd

# Load gold parquet
gold = pd.read_parquet("data/gold/gold_ride_demand.parquet")

# Extract window start & end (nanoseconds → datetime)
gold["window_start"] = pd.to_datetime(gold["window"].apply(lambda x: x["start"]), unit="ns")
gold["window_end"] = pd.to_datetime(gold["window"].apply(lambda x: x["end"]), unit="ns")

# Drop nested column
gold = gold.drop(columns=["window"])

# Reorder columns (clean for BI)
gold = gold[["window_start", "window_end", "pickup_zone", "count"]]

# Save BI-ready version
gold.to_parquet(
    "data/gold/gold_ride_demand_bi.parquet",
    index=False
)

print("BI-ready Gold table created")
print(gold.head())
