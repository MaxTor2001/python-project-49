import prompt
from brain_games.games import calc, even, gcd, prime, progression

def launch_game(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game_module.DESCRIPTION)

    count = 0
    