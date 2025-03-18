import math
import random

DESCRIPTION = 'FinFind the greatest common divisor of given numbers.'


count = 0
while count < 3:
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    right_answer = math.gcd(number_1, number_2)
    while True:
        try:
            question = (
                f"Find the greatest common divisor of given numbers.\n"
                f"Question: {number_1} {number_2} "
            )
            user_answer = float(input(question))
            break
        except ValueError:
            print('Incorrect input. Please enter "number".')
    if right_answer == user_answer:
        print("Correct!")
        count += 1
    else:
        print(
            f"'{user_answer}' is wrong answer ;(. "
            f"Correct answer is '{right_answer}'."
        )
        print(f"Let's try again, {name}!")
        break

if count == 3:
    print(f"Congratulations, {name}!")