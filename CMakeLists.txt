# Set the minimum version of CMake required
cmake_minimum_required(VERSION 3.10)

# Project name and language
project(WarDataFetcher LANGUAGES CXX)

# Define the Python executable
# Ordinarily, I'd do this:
#find_package(Python3 REQUIRED)
#But often its better to juse use pyenv
execute_process(COMMAND pyenv which python OUTPUT_VARIABLE Python3_EXECUTABLE OUTPUT_STRIP_TRAILING_WHITESPACE)


# Define Lua executable path if not on system PATH
set(LUA_EXECUTABLE "/usr/local/bin/lua")

# Add the Python scripts to be run
add_custom_target(build_db
	COMMENT "python3:${Python3_EXECUTABLE}"
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/scripts/build_db.py
    COMMENT "Setting up SQLite database"
)

# Add the Python script for data fetching
add_custom_target(fetch_data
	COMMENT "python3:${Python3_EXECUTABLE}"
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/scripts/fetch_data.py
    DEPENDS build_db  # Ensure this runs after database setup
    COMMENT "Fetching data from sources"
)

# Add the Lua script for rendering data
add_custom_target(render_data
	COMMENT "lua:${LUA_EXECUTABLE}"
    COMMAND ${LUA_EXECUTABLE} ${CMAKE_SOURCE_DIR}/scripts/render_data.lua
    DEPENDS fetch_data  # Ensure this runs after fetching data
    COMMENT "Rendering data from SQLite database"
)

# Optionally, run all steps with a default target
add_custom_target(all_steps
    DEPENDS build_db fetch_data render_data
    COMMENT "Running all stages: build_db, fetch_data, render_data"
)

# Set the default target to all_steps to run everything
set(DEFAULT_TARGET all_steps)

