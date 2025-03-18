<a href="https://codeclimate.com/github/MaxTor2001/python-project-49/maintainability"><img 
src="https://api.codeclimate.com/v1/badges/03c530ba0ac369e38585/maintainability" /></a>

My project - https://github.com/MaxTor2001/python-project-49

To start the project, follow these steps:
1. Check for Ubuntu updates, run the command in the terminal:
- sudo apt update.
Install Python. Run the command in the terminal:
- sudo apt install python3.
2. Install the uv project manager. In the terminal, run the command:
- sudo snap install astral-uv --classic. 
Go to the project directory and run the command:
- uv init.
3. Assemble and install the project. In the terminal, type the commands:
- uv build
- uv tool install dist/*.whl

A brief description of the games:
The user is invited to play a series of games. In order to win, it is necessary to answer three questions correctly in a row. If the user gives an incorrect answer, the game is considered lost and it is necessary to start over.
1. The game: "Parity check". A random number is shown to the user. And he needs to answer yes if the number is even, or no if it is odd. The user must give the correct answer to three questions in a row.
To start the game run: 
- brain-even
2. Game: "Calculator". The user is shown a random mathematical expression that needs to be calculated and the correct answer written down.
To start the game run: 
- brain-calc
3. The NODE game. "Greatest Common Divisor (GCD)". The essence of the game is as follows: the user is shown two random numbers. The user must calculate and enter the largest common divisor of these numbers.
To start the game run: 
- brain-gcd
4. The game "Is a prime number?" The game shows a random number, the user needs to determine whether it is prime and answer yes if the number is prime, or no if not.
To start the game run: 
- brain-progression
5. The game "Arithmetic progression". We show the player a series of numbers that forms an arithmetic progression by replacing any of the numbers with two dots. The player must determine this number.
To start the game run: 
- brain-prime

ASCIINEMA:

brain-even:[![asciicast](https://asciinema.org/a/rok2pwHVEWa8CgUWlsZGw18ga.svg)](https://asciinema.org/a/rok2pwHVEWa8CgUWlsZGw18ga)
brain-calc:[![asciicast](https://asciinema.org/a/BGB6x83eDp6zDnp2GV4fcJlt6)](https://asciinema.org/a/BGB6x83eDp6zDnp2GV4fcJlt6)
brain-gcd:[![asciicast](https://asciinema.org/a/FKt0paXJSRX3HxfkBOh724GDI)](https://asciinema.org/a/FKt0paXJSRX3HxfkBOh724GDI)
brain-progression:[![asciicast](https://asciinema.org/a/g0Cwl9Rfy2S8xlCGwDtiPOSx3)](https://asciinema.org/a/g0Cwl9Rfy2S8xlCGwDtiPOSx3)
brain-prime: [![asciicast](https://asciinema.org/a/8iDI426OeLADrjD2joEIF3plZ)](https://asciinema.org/a/8iDI426OeLADrjD2joEIF3plZ)