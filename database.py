import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('wordle_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store user information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE
    )
''')

# Create a table to store game results
cursor.execute('''
    CREATE TABLE IF NOT EXISTS game_results (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        won BOOLEAN,
        elapsed_time INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()