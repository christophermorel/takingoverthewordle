from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Sample word list
word_list = ["APPLE", "LEMON", "TIGER", "WATER", "SNAKE"]

def get_random_word():
    return random.choice(word_list)

@app.route('/')
def index():
    return render_template('wordle.html')

@app.route('/check_guess', methods=['POST'])
def check_guess():
    data = request.get_json()
    guess = data.get('guess', '').upper()
    correct_word = session.get('correct_word', '')
    
    display = ''
    result = ''
    
    if len(guess) == len(correct_word):
        display = ' '.join(['<span class="correct">{}</span>'.format(c) if c == g else g for c, g in zip(correct_word, guess)])
        if guess == correct_word:
            result = 'Congratulations! You guessed the word!'
        else:
            result = 'Incorrect guess. Try again.'
    else:
        result = 'Invalid guess. Please enter a word with the correct number of letters.'
    
    return jsonify({'display': display, 'result': result})

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)
