import sqlite3
import time
from app import player_name

def create_user(player_name):
    conn = sqlite3.connect('wordle_database.db')
    cursor = conn.cursor()

    # Insert a new user into the 'users' table
    cursor.execute('INSERT INTO users (username) VALUES (?)', (player_name,))
    
    user_id = cursor.lastrowid  # Get the ID of the inserted user
    conn.commit()
    conn.close()
    
    return user_id

def record_game_result(user_id, won):
    conn = sqlite3.connect('wordle_database.db')
    cursor = conn.cursor()

    # Insert a new game result into the 'game_results' table
    start_time = time.time()
    
    # Simulate some game logic here
    
    elapsed_time = int(time.time() - start_time)  # Elapsed time in seconds
    cursor.execute('INSERT INTO game_results (user_id, won, elapsed_time) VALUES (?, ?, ?)',
                   (user_id, won, elapsed_time))

    conn.commit()
    conn.close()

# Example of how to use the functions
user_id = create_user('example_user')
record_game_result(user_id, True)  # User won
