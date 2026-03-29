
import pandas as pd
import numpy as np

class SalesData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Load CSV data into a pandas DataFrame"""
        self.df = pd.read_csv(self.file_path)
        return self.df

    def clean_data(self):
        """Perform basic cleaning steps"""
        if self.df is None:
            raise ValueError("Data not loaded. Run load_data() first.")

        # Convert 'Date' to datetime
        self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')

        # Drop rows with missing Weekly_Sales or Date
        self.df = self.df.dropna(subset=['Weekly_Sales', 'Date'])

        # Fill missing numeric values (Temperature, Fuel_Price, CPI, Unemployment) with median
        numeric_cols = ['Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
        for col in numeric_cols:
            if col in self.df.columns:
                self.df[col] = self.df[col].fillna(self.df[col].median())

        # Ensure correct data types
        self.df['Store'] = self.df['Store'].astype(int)
        self.df['Holiday_Flag'] = self.df['Holiday_Flag'].astype(int)
        self.df['Month'] = self.df['Date'].dt.month
        self.df['Week'] = self.df['Date'].dt.isocalendar().week

        return self.df

    def save_clean_data(self, output_path):
        """Save cleaned data to CSV"""
        if self.df is None:
            raise ValueError("Data not cleaned. Run clean_data() first.")
        self.df.to_csv(output_path, index=False)