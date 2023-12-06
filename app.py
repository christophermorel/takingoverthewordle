import random
import time
from flask import Flask, render_template, request, jsonify
from wordle_wordlist import get_word_list
from cpu import cpu_wordle


app = Flask(__name__)
start_time_dict = {}

# Home route - Renders the title screen or handles form submission
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        player_name = request.form.get('player_name', 'Guest')
        start_time_dict[player_name] = time.time()
        return render_template('wordle.html', player_name=player_name)
    return render_template('index.html')


# Wordle route - Renders the play screen
@app.route('/wordle', methods=['POST'])
def wordle():
    player_name = request.form.get('player_name', 'Guest')
    player_guess = request.form.get('guess', '')
    
    return render_template('wordle.html', player_name=player_name)

# get_winWord route - Route for getting a random word
@app.route('/get_winWord')
def get_winWord():
    winWord = random.choice(get_word_list())
    return jsonify({'word': winWord})

if __name__ == '__main__':
    app.run(debug=True)


    
