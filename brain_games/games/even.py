import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


count = 0
while count < 3:
    number = random.randint(0, 1000)
    print('Question:', number)
    
    while True:
        user_answer = input('Your answer: ').lower()
        if user_answer in ['yes', 'no']:
            break
        else:
            print('Incorrect input. Please enter "yes" or "no".')

    if (
        (user_answer == 'yes' and number % 2 == 0)
        or 
        (user_answer == 'no' and number % 2 != 0)
    ):
        print('Correct!')
        count += 1
    else:
        right_answer = 'yes' if number % 2 == 0 else 'no'
        print(
            f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{right_answer}'."
            )
        print(f"Let's try again, {name}!")
        break
    
if count == 3:      
    print(f"Congratulations, {name}!")


