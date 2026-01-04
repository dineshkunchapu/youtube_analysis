import pandas as pd
import os
from googleapiclient.discovery import build
from config import API_KEY

print("API Key loaded:", API_KEY[:6], "*****")  # debug

def fetch_trending_videos(api_key, max_results=100):
    youtube = build("youtube", "v3", developerKey=api_key)
    print("YouTube client created")

    videos = []

    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode="IN",
        maxResults=50
    )

    response = request.execute()
    print("API response received")

    for item in response["items"]:
        videos.append({
            "video_id": item["id"],
            "title": item["snippet"]["title"],
            "channel_title": item["snippet"]["channelTitle"],
            "published_at": item["snippet"]["publishedAt"],
            "view_count": item["statistics"].get("viewCount", 0),
            "like_count": item["statistics"].get("likeCount", 0),
            "comment_count": item["statistics"].get("commentCount", 0),
            "duration": item["contentDetails"]["duration"],
            "category_id": item["snippet"]["categoryId"]
        })

    print("Videos fetched:", len(videos))
    return videos

if __name__ == "__main__":
    data = fetch_trending_videos(API_KEY)
    df = pd.DataFrame(data)
    print(df.head())


    # get current script directory
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # build correct path to data/raw folder
    output_path = os.path.join(base_dir, "..", "data", "raw", "trending_videos.csv")

    # create folder if it does not exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # save csv
    df.to_csv(output_path, index=False)

    print("CSV file saved successfully at:")
    print(output_path)

    print("CSV file saved")
