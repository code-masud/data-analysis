import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    # convert date column
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # drop duplicates
    df = df.drop_duplicates()

    # handling missing value
    df = df.dropna()

    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Week'] = df['Date'].dt.isocalendar().week

    return df

def save_clean_data(df, path):
    df.to_csv(path, index=False)

if __name__ == "__main__":
    input_path = "../data/Walmart_Sales.csv"
    output_path = "../data/cleaned_Walmart_Sales.csv"

    df = load_data(input_path)
    df_clean = clean_data(df)
    save_clean_data(df_clean, output_path)

    print("Data cleaning completed and saved.")
    