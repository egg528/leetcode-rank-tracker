import pandas as pd
import os
from tracker.meta.singleton import SingletonMeta


class RankHandler(metaclass=SingletonMeta):
    _COLUMNS = ['date', 'rank']
    _CSV_PATH = 'tracker/output/{}.csv'

    def __init__(self, username: str):
        if not hasattr(self, '_initialized'):
            self._file_path = self._CSV_PATH.format(username)
            self._load_or_create_csv()
            self._initialized = True

    def _load_or_create_csv(self) -> None:
        if os.path.exists(self._file_path):
            self.df = pd.read_csv(self._file_path)
            self.df['date'] = pd.to_datetime(self.df['date']).dt.strftime('%Y-%m-%d')
        else:
            self.df = pd.DataFrame(columns=self._COLUMNS)
            self.df.to_csv(self._file_path, index=False)

    def upsert(self, date: str, rank: int) -> None:
        date = pd.to_datetime(date).strftime('%Y-%m-%d')
        if date in self.df['date'].values:
            self.df.loc[self.df['date'] == date, 'rank'] = rank
        else:
            new_row = pd.DataFrame({'date': [date], 'rank': [rank]})
            self.df = pd.concat([self.df, new_row], ignore_index=True)

        self.df.to_csv(self._file_path, index=False)

    def find_recent_ranking(self) -> pd.DataFrame:
        self.df['date'] = pd.to_datetime(self.df['date'])
        recent_df = self.df.sort_values(by='date', ascending=False).head(10)
        recent_df = recent_df.reset_index(drop=True)
        return recent_df

    def is_new_rank(self, date: str, rank: int) -> bool:
        if self.df.empty:
            return True

        date = pd.to_datetime(date).strftime('%Y-%m-%d')
        recent_row = self.df.sort_values(by='date', ascending=False).iloc[0]
        recent_date = recent_row['date']
        recent_rank = recent_row['rank']

        if recent_date != date or recent_rank != rank:
            return True

        return False
