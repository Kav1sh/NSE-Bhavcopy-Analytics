from pathlib import Path
import pandas as pd

def raw_data_path():
    raw_folder = Path("data/raw")
    csv_files = list(raw_folder.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError("No CSV file found in data/raw")
    if len(csv_files)>1:
        raise ValueError(f"Multiple CSV files found: {csv_files}")
    csv_path = csv_files[0]
    return csv_path
def load_data():
    csv_path = raw_data_path()
    df = pd.read_csv(csv_path, dtype=str)
    return df




if __name__ ==" __main__":
    df = load_data()
    print("Shape:", df.shape)
    print("\nFirst 5 records:")
    print(df.head())
    print("\nDataset information:")
    df.info()
    print("\nColumn names:")
    print(df.columns.tolist())
    print("\nmissing values")
    print(df.isnull().sum())


    missing_series = df[df["SctySrs"].isna()]
    print("\n --- RECORDS WITH MISSING SECURITY SERIES ---")
    print(missing_series[["TckrSymb", "FinInstrmTp", "FinInstrmNm", "ISIN"]].to_string())

    print(df["SctySrs"].value_counts(dropna=False))
    print(df["FinInstrmTp"].value_counts(dropna=False))