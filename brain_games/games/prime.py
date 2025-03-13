import random

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_user_answer(number):
    """Get the user's answer and validate it."""
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
    """Check if the user's answer is correct."""
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

def welcome_user():
    """Welcome the user and start the game."""
    name = input("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!")
    count = 0
    while count < 3:
        number = random.randint(2, 3571)
        user_answer = get_user_answer(number)
        if check_answer(number, user_answer):
            count += 1
        else:
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f"Congratulations, {name}!")

welcome_user()