import random

def welcome_user():
    name = input("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!")

    count = 0
    while count < 3:
        # Generate a random number
        number = random.randint(0, 1000)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print('Question:', number)
        
        # Validate user input
        while True:
            answer = input('Your answer: ').lower()
            if answer in ['yes', 'no']:
                break
            else:
                print('Incorrect input. Please enter "yes" or "no".')

        # Check if the answer is correct
        if (answer == 'yes' and number % 2 == 0) or (answer == 'no' and number % 2 != 0):
            print('Correct!')
            count += 1
        else:
            # Handle incorrect answers
            correct_answer = 'yes' if number % 2 == 0 else 'no'
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}")
            count = 0

    print(f"Congratulations, {name}!")

welcome_user()