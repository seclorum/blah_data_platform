war_data_platform/
│
├── README.md                  # Project description and setup instructions
├── requirements.txt           # Python dependencies
├── scripts/                   # Data collection and transformation scripts
│   ├── fetch_sources.py   # Fetch some data from open sources 
│   ├── sqlite_schema.sql  # Common database 
│   └── render_data.lua    # Render the data somehow
└── data/                      # Run-time data directory, not included in repo
