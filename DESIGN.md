BACKEND DEVELOPMENT (James Pelaez, Noel Mendez)

List of words
Wordle_wordlist.py is a python repository file with a function get_word_list() returning a list of all the valid 5-lettered words a player is able to guess. 

Cpu.py
Cpu.py is the CP-opponent playing against the player. The function match_feedback(word, guess, feedback) returns a number, in string form, depending on get_feedback(). The function get_feedback(secretWord, guess) iterates through the length of the secret word and checks if the letter of each index within the secret word matches with the corresponding index of the cpu’s guess. “1” means the letter is in the exact spot, “2” means the letter is in the wrong spot, and “0”  means the letter is not in the word. The string of numbers is finally returned. Process_feedback() iterates through the possible words, checks if they match the feedback, and returns a list of the new words that match. The function cpu_wordle(secretWord) will take the list of possible words, keep track of tries, and while tries are under 6 will return the integer of tries it took, or 0 if it did not guess the word.

App.py
The function app.py is a python file that creates a web-based emulation of a word game using Flask, that allows players to guess a secret word and record their game results in a database.
The function app.py is a python file importing flask, random, sqlite3, time, and importing two functions from cpu.py and wordle_wordlist.py. An SQL database is initialized at the beginning of the file to store game results in record_game_result(player_name, elapsed_time), once the server runs. A global variable, secret, is chosen at random from the word list. The global variable, cpu_tries, returns the number of tries it took the cpu to guess the word, or if the cpu did not guess the word (called cpu.py). Additionally, a variable, word_list, is initialized as the list of words in get_word_list(). 

Function Index()
The index route, if it is a POST request, allows the player to enter their names and then redirects the user to the ‘wordle’ route using the ‘url_for’ game page with the name as parameters.
The route, if it is a GET request (when user initially visits the page) will fetch the top 15 game results (player names and elapsed times) from the game_results table in the SQL database. These results are ordered by elapsed time in ascending order. The function finally renders the index.html template, passing the fetched game results as the ‘game_results’ variable, which is used to display the top game results on the index page.

Function Wordle()
If the information that our wordle function is receiving is a “POST” request, then we know that the user has just input their name and so we must start the game. We store the user’s name as well as the time at which the game starts, these are for scoreboard purposes. We then check to see if the time is empty, so that we can convert the value to a float, if it is 0 we set it equal to the current time. 
We initialize guess variable to james as a little easter egg, right after its value is changed to the actual guess a user makes. We then check to see if the user’s guess is part of our word list, similar to The NYT game where you can only input a guess that is the word list they have, if it’s not in the list we don’t allow the input. Our variable checks is defined by us calling our create_check_data() passing the parameters of secret and guess, secret being the correct word and guess being the user’s guess. We then append the user’s guess and checks to our lists of guesses_data and checks_data which are initially empty. If the user’s guess equals the correct word then we calculate the elapsed_time which is the current time minus start_time which was the time that a user started playing the game. We then reset the variables of start_time, secret, checks_data, and guesses_data because the game is over if the user guesses correctly. We render the template of game_over.html with a statement telling them that they won because they guessed the right words as well as the amount of tries it took the cpu to guess the word. 
We have an elif statement checking if the length of the tries is longer than 6 because if they are inputting more than 6 guesses then the game is over and they haven’t guessed the correct word. We reset the elapsed time because their score doesn’t matter if they didn’t guess the word. We then set lost_messge as a statement telling them the correct word as long as the amount of tries it took the cpu. We then reset the variables of secret, guesses_data, checks_data, and start_time. Finally, we return game_over.html with the lost_message so that it can be displayed. 

The final return render_template is in place in case no other conditionals run and we simply just return our wordle.html page.  


Function Create_check_data()
The create_check_data(secret, guess) function takes two parameters, ‘secret’ and ‘guess’, and returns a string representing the feedback for that guess. The ‘guess’ and secret ‘word’ variable are converted to lowercase to avoid confusion, and copies the secret word as ‘word’ for future reference. The first for loop checks for correct positions, by iterating through each character position in the guess, then checking if the character in the guess is in the same position (exact same index) in ‘word’. If true, the corresponding character is capitalized in ‘guess’ and removes the corresponding character from ‘word’. The second loop checks for incorrect positions. The loop iterates through each character position in the guess again and checks if the character in the guess is lowercase (so it is not EXACTLY matching the secret word). Then it checks if the character is present in the remaining characters of ‘word’. If this is true, the character is removed from ‘word’ and the letter stays in the guess, otherwise, it replaces the character in the guess with a hyphen(“-”). Finally, the modified guess will be returned, where correctly positioned characters are capitalized, incorrectly positioned characters are replaced with hyphens, and correct characters not in the correct position are unchanged.

Function record_game_result()
The record_game_result function at the bottom simply takes the user’s name and their elapsed time if they won and adds it to our database. This database is the table displayed in index.html after the user has won one game. 

FRONTEND DEVELOPMENT / BACKEND INTEGRATION (Chris Morel)
Index.html 
	Our index.html is the first page that a user sees when they run our website. It has an input box that allows the user to input their name and then submit it so that our backend can receive their name and then redirect them to our wordle.html page. 
	Under the input box, there is a table present if and only if the website has already run and holds the high scores of other users, which is essentially whoever guesses a word in the least amount of time in seconds. 

Wordle.html 
Our Wordle.html is the main part of our program, it is where a user plays the actual game. The wordle.html page is only loaded on the user’s screen until after they submit their name in index.html. 
The wordle.html has a text box which allows the user to input their guess of what the correct word is. Jinja logic is used to compare the guessed word with the hashed word outputted by the check function. Each word is parsed through and compared to the check function’s output. It is then formatted to the respective class. Then, that guess is printed on the screen, with visual feedback. If a letter is formatted green that means it’s in the actual word and it’s currently in the correct spot. If a letter is formatted orange that means it’s in the actual word but it’s currently in the wrong spot, and if a letter is formatted red it’s not in the word. The screen will continue to print the user’s guess with feedback until they’ve guessed the correct word or until they’re out of tries (6). Once the user gets the word, or they’ve used up all their tries, they are then redirected to the Game_over.html page. 

Game_over.html
	Our game_over.html page is simply the page that loads after the game is over. The page has a box that tells the user congrats if they’ve guessed correctly and then tells them the amount of tries it took the cpu to get the word. 
	If the user didn’t guess the word, then the screen loads the correct word as well as the number of tries it took the cpu to get the word. 
	From this page, we redirect the user to index.html if they wish to play again. Since they have now played, they will see the scoreboard if it was not there before. 

Worldle.css
Index.css
Both of these files contain the formatting necessary to accurately display the game information in a modern fashion
