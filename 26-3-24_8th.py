import pandas as pd

posts = [
    {"post_id": 1, "likes": 25},
    {"post_id": 2, "likes": 18},
    {"post_id": 3, "likes": 35},
    {"post_id": 4, "likes": 12},
    {"post_id": 5, "likes": 22},
    {"post_id": 6, "likes": 30},
    {"post_id": 7, "likes": 40},
    {"post_id": 8, "likes": 15},
    {"post_id": 9, "likes": 28},
    {"post_id": 10, "likes": 20}
]

df = pd.DataFrame(posts)

likes_freq = df["likes"].value_counts().sort_index()

print("Frequency Distribution of Likes:")
for likes, freq in likes_freq.items():
    print(f"{likes} likes: {freq} posts")
