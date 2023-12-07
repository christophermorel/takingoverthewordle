import sqlite3
import time

def record_game_result(name, won):
    conn = sqlite3.connect('wordle_database.db')
    db = conn.cursor()

    # Insert a new game result into the 'game_results' table
    start_time = time.time()
    
    # Simulate some game logic here
    
    elapsed_time = int(time.time() - start_time)  # Elapsed time in seconds
    db.execute('INSERT INTO game_results (name, won, elapsed_time) VALUES (?, ?, ?)',
                   (name, won, elapsed_time))

    conn.commit()
    conn.close()

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('wordle_database.db')
db = conn.cursor()

# Create a table to store game results
db.execute('''
    CREATE TABLE IF NOT EXISTS game_results (
        id INTEGER PRIMARY KEY,
        name TEXT,
        won BOOLEAN,
        elapsed_time INTEGER
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

# Example of how to use the function
# record_game_result('example_user', True)  # User won