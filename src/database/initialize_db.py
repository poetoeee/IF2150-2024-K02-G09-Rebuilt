import sqlite3
import os

db_dir = os.path.dirname(__file__)
db_file = 'rebuilt.db'
db_path = os.path.join(db_dir, db_file)

def initialize_db():
    with sqlite3.connect(db_path) as conn:
        with open(os.path.join(db_dir, 'schema.sql'), 'r') as f:
            conn.executescript(f.read())

if __name__ == "__main__":
    initialize_db()
    print("Database initialized successfully.")
