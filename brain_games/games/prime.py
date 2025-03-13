import random

def is_prime(n):
    """Check if number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def welcome_user():
    name = input("Welcome to Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!")
    count = 0
    while count < 3:
        number = random.randint(2, 3571)
        user_answer = input(
            f"Is {number} prime? (yes/no): "
        ).lower()
        while user_answer not in ['yes', 'no']:
            print("Invalid input. Enter yes or no.")
            user_answer = input(
                f"Is {number} prime? (yes/no): "
            ).lower()
        if (is_prime(number) and user_answer == 'yes') or \
           (not is_prime(number) and user_answer == 'no'):
            print("Correct!")
            count += 1
        else:
            correct_answer = 'yes' if is_prime(number) else 'no'
            print(f"Wrong answer. Correct answer was {correct_answer}.")
            print(f"Try again, {name}!")
            break
    if count == 3:
        print(f"Congratulations, {name}!")

welcome_user()