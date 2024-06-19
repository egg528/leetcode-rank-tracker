import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator

class RankingGraphGenerator:
    _SAVE_PATH = 'tracker/output/{}.png'

    def __init__(self, username: str):
        self._file_path = self._SAVE_PATH.format(username)

    def generate(self, df: pd.DataFrame) -> None:
        df['rank'] = pd.to_numeric(df['rank'], errors='coerce').fillna(0).astype(int)

        plt.figure(figsize=(12, 8))
        plt.plot(df['date'], df['rank'], marker='s', linestyle='--', color='green', linewidth=2, markersize=8)
        plt.xlabel('Date', fontsize=14)
        plt.ylabel('Rank', fontsize=14)
        plt.title('LeetCode Ranking', fontsize=16)
        plt.grid(True, which='both', linestyle=':', linewidth=0.5, color='black')

        plt.xticks(rotation=45, fontsize=12)
        plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=10))
        plt.gca().xaxis.set_major_formatter(
            FuncFormatter(lambda x, _: df['date'][int(x)] if int(x) < len(df['date']) else ''))

        plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=10))
        plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))

        for i in range(len(df)):
            plt.annotate(f'{df["rank"][i]:,}', (df['date'][i], df['rank'][i]), textcoords="offset points",
                         xytext=(0, 10), ha='center')

        plt.tight_layout()

        plt.savefig(self._file_path, dpi=300)
        plt.close()