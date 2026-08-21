import sqlite3
import pandas as pd
from pathlib import Path

# Connect to database
conn = sqlite3.connect("sql/berka_bank.db")

# Data folder
data_folder = Path("data")

# CSV files
files = [
    "account",
    "card",
    "client",
    "disp",
    "district",
    "loan",
    "order",
    "trans"
]

for file in files:
    print(f"Importing {file}...")

    df = pd.read_csv(
        data_folder / f"{file}.csv",
        sep=";"
    )

    df.to_sql(
        file,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"{file} imported successfully!")

conn.close()

print("All tables imported successfully!")