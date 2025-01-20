import os

# Base directory for data storage
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Directory to store database and fetched data
DATA_DIR = os.path.join(BASE_DIR, "data")

# Database file path
DB_FILE = os.path.join(DATA_DIR, "war_data.db")

# Ensure the data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Source URLs for data fetching
SOURCES = {
    "ACLED": "https://api.acleddata.com/example",
    "UCDP": "https://ucdp.uu.se/api/example",
    "GTD": "https://www.start.umd.edu/gtd/api/example",
    "WHO": "https://who.int/api/example",
    "PRIO": "https://prio.org/api/example"
}

