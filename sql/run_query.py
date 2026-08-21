import sqlite3
import pandas as pd

conn = sqlite3.connect("sql/berka_bank.db")

query = """
SELECT name
FROM sqlite_master
WHERE type='table';
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()