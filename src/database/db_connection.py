import sqlite3
import os

db_dir = os.path.dirname(__file__)
db_file = 'rebuilt.db'
db_path = os.path.join(db_dir, db_file)

os.makedirs(db_dir, exist_ok=True)

def get_connection():
    try:
        print(f"Connecting to database at {db_path}")
        connection = sqlite3.connect(db_path)
        connection.execute("PRAGMA foreign_keys = ON;")
        return connection
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None
