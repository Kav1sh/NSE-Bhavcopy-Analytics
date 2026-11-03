from pathlib import Path
import pandas as pd
from inspect_raw import load_data

def clean_data(df):
    df = df[
        (df["SctySrs"] == "EQ")
    ].copy()
 
    required_columns = [
        "TradDt",
        "BizDt",
        "Sgmt",
        "ISIN",
        "TckrSymb",
        "SctySrs",
        "FinInstrmNm",
        "OpnPric",
        "HghPric",
        "LwPric",
        "ClsPric",
        "LastPric",
        "PrvsClsgPric",
        "SttlmPric",
        "TtlTradgVol",
        "TtlTrfVal",
        "TtlNbOfTxsExctd"
    ]
    df = df[required_columns].copy()
    
    
    
    text_columns = df.select_dtypes(include="object").columns
    for column in text_columns:
        df[column] = df[column].str.strip()



    date_columns = ["TradDt", "BizDt"]
    for column in date_columns:
        df[column] = pd.to_datetime(df[column],
                                    errors = "coerce")

    numeric_columns = [
        "OpnPric",
        "HghPric",
        "LwPric",
        "ClsPric",
        "LastPric",
        "PrvsClsgPric",
        "SttlmPric",
        "TtlTradgVol",
        "TtlTrfVal",
        "TtlNbOfTxsExctd"
    ]
    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )
    required_fields = [
        "TradDt",
        "ISIN",
        "TckrSymb",
        "OpnPric",
        "HghPric",
        "LwPric",
        "ClsPric"
    ]

    before = len(df)

    df = df.dropna(subset=required_fields).copy()

    after = len(df)

    print("\nRecords removed:", before - after)

    before = len(df)
    df = df.drop_duplicates().copy()
    after = len(df)
    print("\nExact duplicate records removed:", before - after)

    invalid_ohlc = df[
        (df["HghPric"] < df["LwPric"]) |
        (df["OpnPric"] > df["HghPric"]) |
        (df["OpnPric"] < df["LwPric"]) |
        (df["ClsPric"] > df["HghPric"]) |
        (df["ClsPric"] < df["LwPric"])
    ]

    print("Invalid records:", len(invalid_ohlc))
    return df

if __name__ == "__main__":
    df = load_data()
    cleaned_df = clean_data(df)

    print("\nCleaning completed!")
    print("Final shape:", cleaned_df.shape)
    print(cleaned_df.head())
    output_path = Path("data/processed/nse_cleaned.csv")
    cleaned_df.to_csv(output_path, index=False)

    print("\nCleaned data saved successfully!")