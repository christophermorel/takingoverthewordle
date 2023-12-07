# To be updated
from flask import Flask, render_template, request
import copy

app = Flask(__name__)

def process_guess(guess, past_guesses):
    correct_word = 'PYTHON'  # Replace this with the actual correct word
    correct_class = 'incorrect'
    correct_positions = 0
    correct_letters_count = {}

    result = []

    # Ensure only alphabetical letters are considered in the guess
    guess = ''.join(filter(str.isalpha, guess)).upper()

    for index, letter in enumerate(guess):
        if index < len(correct_word):
            if letter == correct_word[index]:
                correct_positions += 1
                correct_class = 'correct-position'
            elif letter in correct_word:
                if correct_letters_count.get(letter, 0) < correct_word.count(letter):
                    correct_class = 'correct-word'
                    correct_letters_count[letter] = correct_letters_count.get(letter, 0) + 1
            result.append({'letter': letter, 'class': correct_class})

    past_guesses.append(copy.deepcopy(result))  # Append a deep copy to avoid modifying the same list reference

    return result, correct_word

@app.route('/', methods=['GET', 'POST'])
def wordle_game():
    past_guesses = []

    if request.method == 'POST':
        user_guess = request.form.get('user_guess', '')
        current_guess, correct_word = process_guess(user_guess, past_guesses)
        print("Current Guess:", current_guess)  # Debugging line
    else:
        # If the form is not submitted, provide a default value for correct_word
        correct_word = 'PYTHON'

    print("Past Guesses:", past_guesses)  # Debugging line
    return render_template('wordle_table.html', past_guesses=past_guesses, correct_word=correct_word)

if __name__ == '__main__':
    app.run(debug=True)
