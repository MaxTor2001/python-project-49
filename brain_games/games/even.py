from random import randint

# Game constants
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
STOP = 100

def is_even(number):
    return number % 2 == 0

def generate_question_and_answer():
    number = randint(START, STOP)
    question = f'{number}'

    correct_answer = 'yes' if is_even(number) else 'no'

    return question, correct_answer


