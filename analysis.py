import csv
import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV file
def load_data(file_path):
    titles = []
    views =[]
    likes = []
    comments = []

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                view_count = float(row['view_count'])
                like_count = float(row['like_count'])
                comment_count = float(row['comment_count'])
            except ValueError:
                # Skip rows with invalid data
                continue

            # skip videos with zero views to avoid division by zero
            if view_count == 0:
                continue

            titles.append(row['Title'])
            views.append(view_count)
            likes.append(like_count)
            comments.append(comment_count)

    # Convert lists to numpy arrays for analysis
    views = np.array(views)
    likes = np.array(likes)
    comments = np.array(comments)

    return titles, views, likes, comments

# Compute engagement metrics
def compute_engagement(views, likes, comments):
    # Safe engagement computation
    engagment = (likes + comments) / views
    return engagment

# Get top N videos by engagement
def get_top_videos(titles, engagment, top_n=10):
    top_indices = np.argsort(engagment)[-top_n:][::-1]
    top_titles = [
        titles[i][:20] + '...' if len(titles[i]) > 20 else titles[i] 
        for i in top_indices
        ]
    top_engagement = engagment[top_indices]
    return top_titles, top_engagement

# Detect Viral Videos
def detect_viral(engagement):
    threshold = np.mean(engagement) + 2 * np.std(engagement)
    viral_indices = np.where(engagement > threshold)[0]
    return viral_indices, threshold

# Visualization
def plot_top_videos(titles, scores, file_name='top_10_engaging_videos.png'):
    plt.figure(figsize=(10, 6))
    plt.barh(titles, scores, color='green')
    plt.xlabel('Engagement Rate')
    plt.ylabel('Video Title')
    plt.title('Top 10 Engaging Videos')
    plt.gca().invert_yaxis() # Invert y-axis to show the highest engagement at the top
    plt.tight_layout()
    plt.savefig(file_name)
    plt.show()

# Main pipeline
if __name__ == "__main__":
    # 1. Load Data
    file_path = 'youtube_recommendation_dataset.csv'
    titles, views, likes, comments = load_data(file_path)

    # 2. Compute Engagement
    engagement = compute_engagement(views, likes, comments)

    # 3. Get Top 10 Videos
    top_titles, top_engagement = get_top_videos(titles, engagement, top_n=10)
    print("Top 10 Engaging Videos:")
    for title, score in zip(top_titles, top_engagement):
        print(f"{title}: {score:.4f}")

    # 4. Plot Top Videos
    plot_top_videos(top_titles, top_engagement)

    # 5. Detect Viral Videos
    viral_indices, threshold = detect_viral(engagement)
    print(f"\nViral Video Threshold: {threshold:.4f}")
    print(f"Number of Viral Videos: {len(viral_indices)}")

    # 6. Display some statistics
    print(f"\nDataset Statistics:")
    print(f"Average Engagement: {np.mean(engagement):.4f}")
    print(f"Max Engagement: {np.max(engagement):.4f}")
    print(f"Median Engagement: {np.median(engagement):.4f}")
