import pandas as pd
from functools import lru_cache

CSV_FILE = r"sample.csv"

@lru_cache(maxsize=8)
def fetch_csv(file_path=CSV_FILE):
    """Fetch CSV from local file and cache it."""
    return pd.read_csv(file_path)

# Optional preview
if __name__ == "__main__":
    df = fetch_csv()
    print(df.head())
