import random

def welcome_user():
    name = input("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!")

    count = 0
    while count < 3:
        array_of_numbers = random.randint(0,1000)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print('Question:', array_of_numbers)
        while True:
            answer = str(input('Your answer: ')).lower()
            if answer == 'yes' or answer == 'no':
                break
            else:
                print('Incorrect input. Please enter "yes" or "no".')
        if answer == 'yes' and array_of_numbers % 2 == 0 or answer == 'no' and array_of_numbers % 2 !=0:
            print('Correct!')
            count += 1
        if answer == 'yes' and array_of_numbers % 2 != 0:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}")
            count = 0
            continue
        if answer == 'no' and array_of_numbers % 2 == 0:
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}")
            count = 0
            continue
    print(f"Congratulations, {name}!")

welcome_user()