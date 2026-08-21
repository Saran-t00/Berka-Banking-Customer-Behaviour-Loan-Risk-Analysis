import sqlite3
from pathlib import Path

# Database path
db_path = Path("sql") / "berka_bank.db"

# Create connection
conn = sqlite3.connect(db_path)

print("Database created successfully!")

conn.close()