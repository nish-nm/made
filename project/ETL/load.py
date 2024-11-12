import sqlite3
import pandas as pd
import os

def load_to_sqlite(df, db_path='../data/analysis.db', table_name='US_Analysis'):
    """
    Loads the merged DataFrame into an SQLite database in the data folder.

    Parameters:
    - df (pd.DataFrame): DataFrame to be loaded.
    - db_path (str): Path to the SQLite database file.
    - table_name (str): Name of the table to create in the database.
    """
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Connect to the SQLite database and load data
    with sqlite3.connect(db_path) as conn:
        df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    print(f"Data loaded into '{table_name}' table in '{db_path}'")
