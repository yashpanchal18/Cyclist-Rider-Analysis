import pandas as pd

# Load the already saved dataset
df = pd.read_csv("2024-tripdata.csv")

# Round off 'ride_length' to the nearest whole number
df['ride_length'] = df['ride_length'].round(0).astype(int)

# Save the updated dataset (overwrite the existing CSV)
df.to_csv("2024-tripdata.csv", index=False)

print("Ride length rounded and dataset updated successfully!")
