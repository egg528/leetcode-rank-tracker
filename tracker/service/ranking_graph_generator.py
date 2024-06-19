import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from tracker.meta.singleton import SingletonMeta


class RankingGraphGenerator(metaclass=SingletonMeta):
    _SAVE_PATH = 'tracker/output/{}.png'

    def __init__(self, username: str):
        if not hasattr(self, '_initialized'):
            self._file_path = self._SAVE_PATH.format(username)
            self._initialized = True

    def generate(self, df: pd.DataFrame) -> None:
        df['rank'] = pd.to_numeric(df['rank'], errors='coerce').fillna(0).astype(int)

        plt.figure(figsize=(12, 8))
        plt.plot(df['date'], df['rank'], marker='s', linestyle='--', color='green', linewidth=2, markersize=8)
        plt.xlabel('Date', fontsize=14)
        plt.ylabel('Rank', fontsize=14)
        plt.title('LeetCode rank', fontsize=16)
        plt.grid(True, which='both', linestyle=':', linewidth=0.5, color='black')

        unique_dates = df['date'].unique()
        plt.xticks(unique_dates, rotation=45, fontsize=12)

        unique_ranks = df['rank'].unique()
        plt.yticks(unique_ranks, fontsize=12)

        plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))

        plt.tight_layout()

        plt.savefig(self._file_path, dpi=300)
        plt.close()
