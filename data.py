# this script processes the data

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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
        plt.figure(figsize=(10, 5))
        plt.bar(top_views.index, top_views.values, color=colors(x / N))
        plt.ylabel("Freq", fontsize=12)
        plt.xlabel("Show titles", fontsize=12)
        plt.title("My Top 10 Shows on Netflix based on My Viewing Activity", fontsize=16)
        plt.show()
        return self.file

