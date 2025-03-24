import pandas as pd
import sqlite3

def load_csv(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df

def store_in_sqlite(df: pd.DataFrame, db_path: str = "jobs.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql("jobs", conn, if_exists="replace", index=False)
    conn.close()
    print("Data stored in SQLite")