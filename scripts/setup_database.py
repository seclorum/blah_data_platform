import sqlite3
import os
from config import DB_FILE  # Import the DB_FILE path from config.py

def setup_database():
    """
    Set up SQLite database schema for storing raw data.
    Creates a table for raw data (source, data, and timestamp).
    """
    print(f"Setting up database at {DB_FILE}...")
    
    # Ensure the database directory exists
    db_dir = os.path.dirname(DB_FILE)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
        print(f"Created directory {db_dir}")

    # Connect to SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create table to store raw JSON data from sources
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS raw_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT NOT NULL,
        data TEXT NOT NULL,
        fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    print("Table 'raw_data' created (or already exists).")

    # Optionally, create other tables for normalized data
    # Example: Creating a table for conflict events (This part can be expanded later)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conflict_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT NOT NULL,
        event_date DATE NOT NULL,
        location TEXT NOT NULL,
        fatalities INTEGER,
        details TEXT
    )
    """)
    print("Table 'conflict_events' created (or already exists).")

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print("Database setup complete.")

# Main entry point for the script
if __name__ == "__main__":
    setup_database()

