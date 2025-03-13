import random

def welcome_user():
    name = input("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0
    while count < 3:
        number = random.randint(0, 1000)
        print('Question:', number)
        
        while True:
            answer = input('Your answer: ').lower()
            if answer in ['yes', 'no']:
                break
            else:
                print('Incorrect input. Please enter "yes" or "no".')

        if (answer == 'yes' and number % 2 == 0) or (answer == 'no' and number % 2 != 0):
            print('Correct!')
            count += 1
        else:
            correct_answer = 'yes' if number % 2 == 0 else 'no'
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        
    if count == 3:      
        print(f"Congratulations, {name}!")

welcome_user()