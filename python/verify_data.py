import pandas as pd

silver = pd.read_parquet("data/silver/silver_rides.parquet")
gold = pd.read_parquet("data/gold/gold_ride_demand.parquet")

print("Silver shape:", silver.shape)
print("Gold shape:", gold.shape)

print("\nSilver preview:")
print(silver.head())

print("\nGold preview:")
print(gold.head())
