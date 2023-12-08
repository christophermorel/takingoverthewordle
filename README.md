Taking over the wordle. 

To run the flask server, the vscode extensions, Python (Microsoft), SQLite & MySQL Snippets (Rohit Chouhan), and flask-snippet (cstrap) are needed.
Windows:
1. Set up virtual environment by running "python -m venv venv" in the Integrated Terminal
2. Then execute "venv\Scripts\activate"

MacOs/Linux:
1. Set up virtual environment by running "python3 -m venv venv" in the Integrated Terminal"
2. Then execute "source venv/bin/activate"

3. Install flask into environment by running "pip install flask"
4. cd into "takingoverthewordle" or if renamed, the name of the project directory
5. Run "python3 app.py" and open the Flask development server

6. To kill the development server press Control+C, and to deactive the virtual environment type "deactivate" into the Integrated Terminal

The simplest definition of our project is a recreation of The New York Times’ popular online game “Wordle” with a few twists. Those twists being that you’re playing against a cpu and have to guess the word in less tries, meaning that you lose if the cpu guesses the word in less tries. 

We used Python for backend logic such as creating the CPU and actually choosing the random word within our word list. And we used html/flask/javascript to make a functioning front end which allows the user to input multiple characters as their guess. Ultimately using CSS for the visual aspect of our website so that we could clearly see when a letter was in the correct spot, at least within the word, or not in the word at all. 

When you run the code you will be directed to our home page which quite simply asks the user for their name. The purpose of asking for your name is for our leaderboard/scoreboard system which accounts for how long it takes a user to guess the correct word and beat the cpu.

After you guess the correct word, we will let you know that it’s the correct word, and considering the cpu’s guess we will let you know if you beat the cpu in less tries or not. 

The game is all about a little competitiveness in a harmless game. Make the best player take the Wordle over!  
