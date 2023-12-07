import sqlite3

def connect_db():
    return sqlite3.connect('wordle_database.db')

def record_game_result(name, elapsed_time):
    conn = connect_db()
    db = conn.cursor()

    db.execute('''
        CREATE TABLE IF NOT EXISTS game_results (
        id INTEGER PRIMARY KEY,
        name TEXT,
        elapsed_time REAL
    )
''')

    db.execute('INSERT INTO game_results (name, elapsed_time) VALUES (?, ?)',
                   (name, elapsed_time))

    conn.commit()
    conn.close()
