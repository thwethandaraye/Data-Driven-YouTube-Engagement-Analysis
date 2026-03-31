# YouTube Engagement Analysis v2: Scalable Data Pipeline with NumPy

## Project Overview
This project analyzes YouTube video performance using Python, NumPy, and Matplotlib.  
It identifies the most engaging content by computing engagement metrics, detecting viral videos, and visualizing insights. The analysis is fully vectorized using NumPy for efficient computation, making it scalable to large datasets.

---

## 🔍 Key Features

- **Data Cleaning**: Handles missing or invalid numerical values, and safely computes engagement to avoid division by zero.
- **Vectorized Computation**: Engagement metrics are calculated using NumPy arrays for speed and efficiency.
- **Top Video Analysis**: Identifies top-performing videos based on engagement.
- **Viral Video Detection**: Detects outliers in engagement using statistical thresholds (mean + 2 standard deviations).
- **Visualization**: Generates bar charts for the top videos and histograms for engagement distribution.
- **Statistics**: Provides average, median, and maximum engagement rates.

---

## 📊 Insights from Analysis

- Engagement is not perfectly correlated with views; some videos with fewer views have higher engagement rates.
- Viral videos are statistical outliers, representing a small percentage of total content but a large percentage of engagement.
- Engagement distribution is skewed: most videos perform moderately, with a few high-performing outliers.

---

## 🛠️ Tech Stack

- Python 3
- NumPy (numerical computation)
- Matplotlib (visualization)
- CSV (data handling)

---
## ⚡ How to Run

1. Make sure you have Python 3 installed.
2. Install dependencies (if needed):

```bash
pip install numpy matplotlib
```

3. Run the main analysis:

```bash
python src/analysis.py
```

4. Output:  
Top 10 engaging videos printed to console  
Bar chart saved to output/top_10_engaging_videos.png  
Viral video statistics printed to console  
