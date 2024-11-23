<!-- This is challenge validator script made using python language

Overview:

This is an interactive Python script that simulates a password cracking challenge. The objective is for the participsnt to guess the correct password which is hashed using MD5 encryption. The game provides dynamic hints based on the number of attempts made.

The script is designed to simulate the experience of a "hacker" trying to break a hashed password using hints to guide them to the correct solution.

Features:

1)Dynamic Challenge Selection: The game randomly selects a challenge from a list of predefined challenges.

2)Hash-based Authentication: The solution to the challenge is based on a hashed password (MD5). Users input guesses, and their solutions are hashed and compared to the correct hash.

3)Hint System: The script provides helpful hints to guide the user. The number of hints increases with each failed attempt.

4)Attempts Tracker: Keeps track of the number of attempts, and if the user fails more than 3 times, the game gives a more direct hint.

5)Difficulty Levels: Challenges can be categorized into different difficulty levels (though this script currently has only one challenge, marked "EASY").

The core class that defines the game logic :-

__init__: Initializes the game with predefined challenges.

start_challenge: Randomly selects and displays a challenge.

_generate_hint: Provides dynamic hints based on the number of attempts.

try_solution: Compares the user’s guess to the correct solution and provides feedback.

Main Function: The main() function runs the script, starting the game and testing multiple password attempts.
 -->
