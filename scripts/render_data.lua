-- Lua: Reading SQLite Data and Rendering
local sqlite3 = require("lsqlite3")

-- Connect to SQLite database
local function connect_to_db(db_name)
    local db = sqlite3.open(db_name)
    if not db then
        error("Failed to open database")
    end
    return db
end

-- Fetch raw data from the SQLite database
local function fetch_raw_data(db)
    local raw_data = {}
    for row in db:nrows("SELECT id, source, data, fetched_at FROM raw_data") do
        table.insert(raw_data, row)
    end
    return raw_data
end

-- Render data (simple print output for now)
local function render_data(data)
    print("Rendering Data:")
    for _, entry in ipairs(data) do
        print(string.format("ID: %d, Source: %s, Fetched At: %s", entry.id, entry.source, entry.fetched_at))
        print("Data: " .. entry.data)
    end
end

-- Main function
local function main()
    local db_name = "war_data.db"
    local db = connect_to_db(db_name)
    local raw_data = fetch_raw_data(db)
    render_data(raw_data)
    db:close()
end

main()

