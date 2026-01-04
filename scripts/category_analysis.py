import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- PATH SETUP ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "..", "data", "cleaned_trending_videos.csv")

df = pd.read_csv(data_path)

# ---------------- CATEGORY MAPPING ----------------
category_map = {
    1: "Film & Animation",
    2: "Autos & Vehicles",
    10: "Music",
    15: "Pets & Animals",
    17: "Sports",
    19: "Travel & Events",
    20: "Gaming",
    22: "People & Blogs",
    23: "Comedy",
    24: "Entertainment",
    25: "News & Politics",
    26: "Howto & Style",
    27: "Education",
    28: "Science & Technology"
}

df["category_name"] = df["category_id"].astype(int).map(category_map)

# ---------------- AGGREGATION ----------------
category_views = (
    df.groupby("category_name")["view_count"]
    .sum()
    .sort_values(ascending=False)
)

print(category_views)

# ---------------- VISUALIZATION ----------------
plt.figure(figsize=(10, 6))
sns.barplot(
    x=category_views.values,
    y=category_views.index
)
plt.title("Total Views by YouTube Video Category")
plt.xlabel("Total Views")
plt.ylabel("Category")
plt.tight_layout()
plt.show()
