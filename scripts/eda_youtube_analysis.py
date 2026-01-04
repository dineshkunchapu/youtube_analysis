import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# load cleaned data
data_path = os.path.join(BASE_DIR, "..", "data", "cleaned_trending_videos.csv")
df = pd.read_csv(data_path)

print("Data loaded:", df.shape)

# ---------------- BASIC STATS ----------------
print("\nBasic Statistics:")
print(df[["view_count", "like_count", "comment_count", "engagement_rate"]].describe())

# ---------------- TOP VIDEOS ----------------
print("\nTop 5 videos by views:")
print(df[["title", "view_count"]].sort_values(by="view_count", ascending=False).head())

# ---------------- CORRELATION ----------------
corr = df[["view_count", "like_count", "comment_count"]].corr()
print("\nCorrelation Matrix:")
print(corr)

# ---------------- VISUALS ----------------

# Views distribution
plt.figure()
sns.histplot(df["view_count"], bins=20, kde=True)
plt.title("View Count Distribution")
plt.show()

# Likes vs Views
plt.figure()
sns.scatterplot(x="view_count", y="like_count", data=df)
plt.title("Likes vs Views")
plt.show()

# Engagement Rate Distribution
plt.figure()
sns.histplot(df["engagement_rate"], bins=20)
plt.title("Engagement Rate Distribution")
plt.show()
