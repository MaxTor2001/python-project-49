from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
STOP = 100

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def generate_question_and_answer():
    number = randint(START, STOP)
    question = f'{number}'

    correct_answer = 'yes' if is_even(number) else 'no'

    return question, correct_answer


