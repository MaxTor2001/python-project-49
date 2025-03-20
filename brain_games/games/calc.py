from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'



def generate_question_and_answer():

    operation = choice(['+', '-', '*'])
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    question = f'{num_1} {operation} {num_2}'
    if operation == '+':
        correct_answer = num_1 + num_2
    elif operation == '-':
        correct_answer = num_1 - num_2
    elif operation == '*':
        correct_answer = num_1 * num_2
    return question, str(correct_answer)
