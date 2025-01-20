-- SQLite schema for raw and normalized data storage

-- Table for raw JSON data
CREATE TABLE raw_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,
    data TEXT NOT NULL,
    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for normalized data (an example normalization for conflict events)
CREATE TABLE conflict_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,
    event_date DATE NOT NULL,
    location TEXT NOT NULL,
    fatalities INTEGER,
    details TEXT
);

