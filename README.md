```
blah_data_platform/
│
├── CMakeLists.txt          # CMake configuration file
├── README.md               # Project description and instructions
├── config.py               # Configuration file
├── data/                   # Data storage directory
│   └── blah_data.db         # SQLite database (created during build_db)
└── scripts/
    ├── fetch_data.lua      # Lua script for data fetching
    ├── render_data.lua     # Lua script for rendering data
    ├── build_db.py   # Python script for setting up the database
    └── sqlite_schema.sql   # SQL schema for creating tables
```


A sample project with Python, Lua, sqlite components - build a database, fetch data, render the data.  
