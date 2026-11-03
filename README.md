## Data Setup

This project uses historical NSE (National Stock Exchange of India) Cash Market **CM-UDiFF Common Bhavcopy** data.

### 1. Download the data

1. Visit the [NSE India website](https://www.nseindia.com/).
2. Navigate to the historical reports / Bhavcopy section.
3. Download the required CM-UDiFF Bhavcopy CSV file for the desired trading date.
4. Extract the CSV file if it is inside a ZIP archive.

### 2. Place the CSV file

Save the extracted CSV file inside:

```text
data/raw/
```

**Important:** The current data-loading script expects exactly one CSV file in `data/raw/` at a time.

### 3. Run the project

After placing the CSV file in the raw folder, run the data inspection and cleaning scripts from the project root:

```bash
python src/inspect_raw.py
python src/cleaning.py
```

The cleaned dataset will be generated in:

```text
data/processed/
```

**Note:** Raw NSE data files are not included in this repository. Users must download their own Bhavcopy CSV files.
