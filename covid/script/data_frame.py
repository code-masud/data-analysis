import pandas as pd

class DataFrame:
    def __init__(self, path):
        self.path = path
        self.df = None
        self.data = None

    def load_data(self):
        if not self.path:
            raise ValueError('File not found.')
        self.df = pd.read_csv(self.path)
        return df