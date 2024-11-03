# this script processes the data

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class NetflixUnpacker:
    def __init__(self, file):
        self.file = pd.read_csv(file)

    def work(self):
        real_titles = []
        for title in self.file['Title']:
            title = title.split(":")[0]
            real_titles.append(title)
        self.file = self.file.drop("Title", axis=1)
        self.file.insert(0, "Title", real_titles, True)
        top_views = pd.Series(self.file["Title"]).value_counts().nlargest(10)
        N = len(top_views)
        x = np.arange(N)
        plt.figure(1, figsize=(14, 5))
        colors = plt.get_cmap('viridis')
        plt.bar(top_views.index, top_views.values, color=colors(x / N))
        plt.ylabel("Freq", fontsize=12)
        plt.xlabel("Show titles", fontsize=12)
        plt.title("My Top 10 Shows on Netflix based on My Viewing Activity", fontsize=16)
        plt.savefig("./static/img/fig1.png")

        self.file['date'] = pd.to_datetime(self.file['Date'])
        # self.file['day'] = [d.day for d in self.file.date]
        self.file['day'] = self.file['date'].dt.day_name()

        print(self.file.day)

        cats = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.file.day = pd.Categorical(self.file["day"], categories=cats, ordered=True)
        by_day = self.file.sort_values("day")["day"].value_counts().sort_index()
        print(by_day)

        N = len(by_day)
        x = np.arange(N)
        plt.figure(2, figsize=(10, 5))
        colors = plt.get_cmap("winter").reversed()
        plt.bar(by_day.index, by_day.values, color=colors(x / N))
        plt.title("My Netflix Viewing Activity Pattern by Day", fontsize=16)
        plt.xlabel("day of the week", fontsize=12)
        plt.ylabel('freq', fontsize=12)
        plt.savefig("./static/img/day.png")

        print(self.file)
        monthly_counts = self.file['date'].value_counts().resample('ME').sum()
        print(monthly_counts)
        N = len(monthly_counts)
        colors = plt.cm.viridis(
            np.linspace(0, 1, N))  # You can use other colormaps like 'plasma', 'cool', 'inferno', etc.

        # Plot the line segments with gradient color
        plt.figure(figsize=(12, 6))
        for i in range(N - 1):
            plt.plot(monthly_counts.index[i:i + 2], monthly_counts.values[i:i + 2], color=colors[i], linewidth=2)

        # Add markers to each data point if desired
        plt.scatter(monthly_counts.index, monthly_counts.values, color=colors, s=30, zorder=3)

        plt.xlabel('Month')
        plt.ylabel('Number of Episodes(/Movies) Watched')
        plt.title('Monthly Frequency')
        plt.ylim(bottom=0)  # Start the y-axis from 0
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("./static/img/history.png")
        return self.file
