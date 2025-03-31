import pandas as pd
from datetime import datetime

# List of file paths (Update with actual file paths)
file_paths = [
    "202401-divvy-tripdata.csv",
    "202402-divvy-tripdata.csv",
    "202403-divvy-tripdata.csv",
    "202404-divvy-tripdata.csv",
    "202405-divvy-tripdata.csv",
    "202406-divvy-tripdata.csv",
    "202407-divvy-tripdata.csv",
    "202408-divvy-tripdata.csv",
    "202409-divvy-tripdata.csv",
    "202410-divvy-tripdata.csv",
    "202411-divvy-tripdata.csv",
    "202412-divvy-tripdata.csv",

]

# Load and append all datasets
df_list = [pd.read_csv(file) for file in file_paths]
df = pd.concat(df_list, ignore_index=True)

# Convert timestamps to datetime format
df['started_at'] = pd.to_datetime(df['started_at'])
df['ended_at'] = pd.to_datetime(df['ended_at'])

# Calculate Ride Length in minutes (rounded to 2 decimal places)
df['ride_length'] = (df['ended_at'] - df['started_at']).dt.total_seconds() / 60

# Extract Weekday (1=Monday, 7=Sunday)
df['weekday'] = df['started_at'].dt.weekday + 1  # FIXED

# Extract Month (Numeric format: 1 for January, 12 for December)
df['month'] = df['started_at'].dt.month


# Save the processed dataset as a CSV file
df.to_csv("2024-tripdata.csv", index=False)

print("Final dataset saved: merged_dataset_with_new_columns.csv")
