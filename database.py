import sqlite3
import time

def connect_db():
    return sqlite3.connect('wordle_database.db')

def create_game_results_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS game_results (
            id INTEGER PRIMARY KEY,
            name TEXT,
            won BOOLEAN,
            elapsed_time INTEGER
        )
    ''')

    conn.commit()
    conn.close()

def record_game_result(name, won, elapsed_time):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO game_results (name, won, elapsed_time) VALUES (?, ?, ?)',
                   (name, won, elapsed_time))

    conn.commit()
    conn.close()
