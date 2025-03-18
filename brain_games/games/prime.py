import random

DESCRIPTION = 'nswer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_user_answer(number):
    while True:
        prompt = (
            f'Answer "yes" if given number is prime. Otherwise answer "no".\n'
            f'Question: {number}? '
        )
        user_answer = str(input(prompt))
        if user_answer == 'yes' or user_answer == 'no':
            return user_answer
        else:
            print('Incorrect input. Please enter "yes" or "no".')


def check_answer(number, user_answer):
    if is_prime(number) and user_answer == 'yes':
        print("Correct!")
        return True
    elif is_prime(number) and user_answer == 'no':
        print("'no' is wrong answer ;(. Correct answer was 'yes'.)")
        return False
    elif not is_prime(number) and user_answer == 'yes':
        print("'yes' is wrong answer ;(. Correct answer was 'no'.)")
        return False
    else:
        print("Correct!")
        return True
