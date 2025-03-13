import random
import math

def welcome_user():
    name = input("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!")
    count = 0
    while count < 3:
        number_1 = random.randint(0,100)
        number_2 = random.randint(0,100)
        right_answer = math.gcd(number_1, number_2)
        while True:
            try:
                user_answer = float(input(f"Find the greatest common divisor of given numbers.\nQuestion: {number_1} {number_2} "))
                break
            except ValueError:
                print('Incorrect input. Please enter "number".')
        if right_answer == user_answer:
            print("Correct!")
            count += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer is '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if count == 3:
        print(f"Congratulations, {name}!")

welcome_user()