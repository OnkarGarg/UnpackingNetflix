# this script processes the data

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


class NetflixUnpacker:
    def __init__(self, file):
        self.file = pd.read_csv(file)

    def work(self):
        real_titles = []
        print(self.file)
        for title in self.file['Title']:
            title = title.split(":")[0]
            real_titles.append(title)
            print(title)
        self.file = self.file.drop("Title", axis=1)
        self.file.insert(0, "Title", real_titles, True)
        print(self.file.head())
        top_views = pd.Series(self.file["Title"]).value_counts().nlargest(10)
        N = len(top_views)
        x = np.arange(N)
        colors = plt.get_cmap('viridis')
        plt.figure(figsize=(20, 5))
        plt.bar(top_views.index, top_views.values, color=colors(x / N))
        plt.ylabel("Freq", fontsize=12)
        plt.xlabel("Show titles", fontsize=12)
        plt.title("My Top 10 Shows on Netflix based on My Viewing Activity", fontsize=16)
        plt.savefig("./static/images/fig1.png")

        # self.file['date'] = pd.to_datetime(self.file['Date'])
        # print(self.file['date'])
        # for d in self.file.date:
        #     print(d)
        #     a = datetime.fromtimestamp(d.timestamp())
        #     print(a)
        # self.file['day'] = [datetime.fromtimestamp(d).day for d in self.file['date']]
        #
        # cats = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        # self.file.day = pd.Categorical(self.file["day"], categories=cats, ordered=True)
        # by_day = self.file.sort_values("day")["day"].value_counts().sort_index()
        # plt.style.use("seaborn-darkgrid")
        #
        # N = len(by_day)
        # x = np.arange(N)
        # colors = plt.get_cmap("winter").reversed()
        # plt.figure(figsize=(10, 5))
        # plt.bar(by_day.index, by_day.values, color=colors(x / N))
        # plt.title("My Netflix Viewing Activity Pattern by Day", fontsize=20)
        # plt.xlabel("day of the week", fontsize=15)
        # plt.ylabel('freq', fontsize=15)
        # plt.savefig("day.png", dpi=300, bbox_inches='tight')
        # plt.show()

        return self.file
