# Import configuration
import sqlite3
import requests
import json
from config import DB_FILE, SOURCES

# SQLite schema setup
def build_db():
    """
    Set up SQLite schema with a general table for raw data.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Table to store raw JSON data from each source
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS raw_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT NOT NULL,
        data TEXT NOT NULL,
        fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

# Fetch data from a given source URL
def fetch_data(source_name, url):
    """
    Fetch JSON data from a source URL and return it as a dictionary.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return {"source": source_name, "data": response.json()}
    except requests.RequestException as e:
        print(f"Error fetching data from {source_name}: {e}")
        return None

# Save fetched data into SQLite
def save_data_to_db(source_name, data):
    """
    Save raw JSON data to the SQLite database.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO raw_data (source, data) VALUES (?, ?)", (source_name, json.dumps(data)))
    conn.commit()
    conn.close()

# Main function to fetch and save data from multiple sources
def main():
    #build_db()

    #for source_name, url in SOURCES.items():
        #data = fetch_data(source_name, url)
        #if data:
        #    save_data_to_db(source_name, data["data"])

if __name__ == "__main__":
    main()

