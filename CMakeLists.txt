# Set the minimum version of CMake required
cmake_minimum_required(VERSION 3.10)

# Project name and language
project(WarDataFetcher LANGUAGES CXX)

# Define the Python executable
find_package(Python3 REQUIRED)

# Define Lua executable path if not on system PATH
set(LUA_EXECUTABLE "/usr/local/bin/lua")

# Add the Python scripts to be run
add_custom_target(build_db
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/scripts/setup_database.py
    COMMENT "Setting up SQLite database"
)

# Add the Python script for data fetching
add_custom_target(fetch_data
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/scripts/fetch_data.py
    DEPENDS build_db  # Ensure this runs after database setup
    COMMENT "Fetching data from sources"
)

# Add the Lua script for rendering data
add_custom_target(render_data
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

