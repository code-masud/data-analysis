from pathlib import Path
import pandas as pd


class SalesData:
    def __init__(self, file_path: str):
        self.file_path = self._validate_path(file_path)
        self.df: pd.DataFrame | None = None

    @staticmethod
    def _validate_path(file_path: str) -> Path:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"{file_path} does not exist.")
        if not path.is_file():
            raise ValueError(f"{file_path} is not a valid file.")
        return path

    def load_data(self) -> pd.DataFrame:
        """Load CSV data into a pandas DataFrame"""
        try:
            self.df = pd.read_csv(self.file_path)
            return self.df
        except Exception as e:
            raise RuntimeError(f"Error loading data: {e}")

    def clean_data(self) -> pd.DataFrame:
        """Perform basic cleaning steps"""
        if self.df is None:
            raise RuntimeError("Data not loaded. Run load_data() first.")

        df = self.df.copy()

        # Convert Date
        df['Date'] = pd.to_datetime(df.get('Date'), errors='coerce')

        # Drop invalid rows
        df = df.dropna(subset=['Weekly_Sales', 'Date'])

        # Fill numeric missing values efficiently
        numeric_cols = ['Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
        existing_cols = [col for col in numeric_cols if col in df.columns]
        df[existing_cols] = df[existing_cols].fillna(df[existing_cols].median())

        # Type conversions (safe)
        df['Store'] = pd.to_numeric(df.get('Store'), errors='coerce').astype('Int64')
        df['Holiday_Flag'] = pd.to_numeric(df.get('Holiday_Flag'), errors='coerce').astype('Int64')

        # Feature engineering
        df['Month'] = df['Date'].dt.month
        df['Week'] = df['Date'].dt.isocalendar().week.astype('Int64')

        self.df = df
        return self.df

    def save_clean_data(self, output_path: str) -> None:
        """Save cleaned data to CSV"""
        if self.df is None:
            raise RuntimeError("No data available to save.")
        
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        self.df.to_csv(output_path, index=False)

