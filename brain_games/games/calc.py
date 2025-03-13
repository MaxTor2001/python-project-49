import random
import operator

def welcome_user():
    name = input("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!")


    count = 0
    while count < 3:
        number_1 = random.randint(0,10)
        number_2 = random.randint(0,10)
        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        rand = random.choice(list(operators.keys()))
        answer = operators[rand](number_1, number_2)
        while True:
            try:
                user_answer = float(input(f"What is the result of the expression?\nQuestion: {number_1} {rand} {number_2}? "))
                break
            except ValueError:
                print('Incorrect input. Please enter "number".')
        if abs(user_answer - answer) == 0:
            print("Correct!")
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer is '{answer}'.")
            print(f"Let's try again {name}!")
            break

    if count == 3:
        print(f"Congratulations, {name}!")

welcome_user()