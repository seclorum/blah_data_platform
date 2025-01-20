import sqlite3
import os
from config import DB_FILE  # Import the DB_FILE path from config.py

def read_sql_schema(schema_file):
    """
    Read the SQL schema file and return its content.
    """
    with open(schema_file, 'r') as file:
        return file.read()

def build_db():
    """
    Set up SQLite database schema using the SQL in sqlite_schema.sql.
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

    # Read the schema from the sqlite_schema.sql file
    schema_sql = read_sql_schema(os.path.join(os.path.dirname(__file__), 'sqlite_schema.sql'))
    
    # Execute the schema
    cursor.executescript(schema_sql)
    print("Database schema applied.")

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print("Database setup complete.")

# Main entry point for the script
if __name__ == "__main__":
    build_db()

