import pandas as pd
import os

# get base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# input and output paths
input_path = os.path.join(BASE_DIR, "..", "data", "raw", "trending_videos.csv")
output_path = os.path.join(BASE_DIR, "..", "data", "cleaned_trending_videos.csv")

# load raw data
df = pd.read_csv(input_path)

print("Raw data shape:", df.shape)

# ---------------- CLEANING ----------------

# convert numeric columns
num_cols = ["view_count", "like_count", "comment_count"]
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

# convert publish date
df["published_at"] = pd.to_datetime(df["published_at"])

# remove duplicate videos
df.drop_duplicates(subset="video_id", inplace=True)

# create engagement rate
df["engagement_rate"] = (
    df["like_count"] + df["comment_count"]
) / df["view_count"].replace(0, 1)

print("Cleaned data shape:", df.shape)

# save cleaned data
df.to_csv(output_path, index=False)

print("Cleaned data saved at:")
print(output_path)

print(df.head())
