import csv
import matplotlib.pyplot as plt

# Lists to store video titles and their corresponding engagement rates
video_titles = []
engagement_scores = []

# Open the Dataset.csv file and read its contents
with open("youtube_recommendation_dataset.csv", mode="r", encoding='utf-8') as file:
    # DictReader uses the first row of the CSV as keys
    reader = csv.DictReader(file)

    # Extract Title and Engagement Rate
    data_list = []
    for row in reader:
        # Store the title and engagement rate in a temporary list
        data_list.append({
            "title": row["Title"],
            "engagement_rate": float(row["engagement_rate"])
        })

# Sort data by engagement (Highest to Lowest)
# This says: "Sort data_list based on the 'engagement' value"
data_list.sort(key=lambda x: x['engagement_rate'], reverse=True)

# Take the Top 10 most engaging videos
top_10 = data_list[:10]
print(top_10)

for item in top_10:
    # Shorten the title if it's too long for better visualization
    short_title = item["title"][:20] + "..."
    video_titles.append(short_title)
    engagement_scores.append(item["engagement_rate"])

# Create a bar chart to visualize the top 10 most engaging videos
plt.figure(figsize=(12, 6))
plt.barh(video_titles, engagement_scores, color='green')
plt.xlabel('Engagement Rate')
plt.title('Top 10 Most Engaging YouTube Videos')
plt.gca().invert_yaxis()  # Invert y-axis to show the highest engagement at the top
plt.tight_layout()

# Save the plot as an image file
plt.savefig("top_10_engaging_videos.png")
# Show the plot
plt.show()

print("Analysis complete. The top 10 most engaging videos have been visualized and saved as 'top_10_engaging_videos.png'.")