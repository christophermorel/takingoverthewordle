import random

from flask import Flask, render_template, request
from wordle_wordlist import get_word_list
from cpu.py import cpu_wordle

app = Flask(__name__)

# Home route - Renders the title screen or handles form submission
@app.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        player_name = request.form.get('player_name', 'Guest')
        return render_template('wordle.html', player_name=player_name)
    return render_template('index.html')

# Wordle route - Renders the play screen
@app.route('/wordle', methods=['POST'])
def wordle():
    player_name = request.form.get('player_name', 'Guest')
    return render_template('wordle.html', player_name=player_name)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/wordle')
def wordle():
    guess = request.form.get("guess")
    if guess == winWord:
        winner="you won"
    return render_template('wordle.html', winner=winner)

    
