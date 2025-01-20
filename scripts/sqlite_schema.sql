-- SQLite schema for raw and normalized data storage

-- Table for raw JSON data
CREATE TABLE IF NOT EXISTS raw_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,
    data TEXT NOT NULL,
    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(source, fetched_at)  -- Enforce uniqueness of source/fetch timestamp pair
);

-- Table for normalized data (an example normalization for conflict events)
CREATE TABLE IF NOT EXISTS conflict_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,
    event_date DATE NOT NULL,
    location TEXT NOT NULL,
    fatalities INTEGER,
    details TEXT,
    FOREIGN KEY (source) REFERENCES raw_data (source)  -- Link back to raw_data (optional)
);

-- You could add more tables for other data, e.g., conflict actors, regions, etc.
-- For now, this basic schema supports raw data ingestion and conflict event normalization.

