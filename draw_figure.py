# plot the scores
import pandas as pd
import matplotlib.pyplot as plt

class FigureDisplay():
    """Displays the score chart"""
    def __init__(self, scores, savename="result_score.jpg"):
        self.scores = scores
        self.savename = savename

    def display(self):
        fig, ax = plt.subplots(1, 1, figsize=[10, 5])
        plt.rcParams.update({'font.size': 16})

        scores_rolling = pd.Series(self.scores).rolling(100).mean()
        
        ax.plot(self.scores)
        ax.plot(scores_rolling, c="green", linewidth=3)
        ax.set_xlabel("Episodes")
        ax.set_ylabel("Score")
        ax.grid(which="major")
        ax.axhline(0.5, c="red", linewidth=3)
        ax.legend(["Scores of Episodes", "Last 100 Episode average", "Goal: Score=0.5"])

        fig.savefig(self.savename)