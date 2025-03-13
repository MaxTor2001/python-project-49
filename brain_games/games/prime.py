import random

def welcome_user():
    name = input("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!")

    count = 0
    while count < 3:
        number = random.randint(2, 3571)

        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) +1):
                if n % i == 0:
                    return False
            return True
        
        while True:
            user_answer = str(input(f'Answer "yes" if given number is prime. Otherwise answer "no".\nQuestion: {number}?'))
            if user_answer == 'yes' or user_answer == 'no':
                break
            else:
                print('Incorrect input. Please enter "yes" or "no".')

        if is_prime(number) and user_answer == 'yes':
            print("Correct!")
            count += 1
        elif is_prime(number) and user_answer == 'no':
            print ("'no' is wrong answer ;(. Correct answer was 'yes'.)")
            break
        elif not is_prime(number) and user_answer == 'yes':
            print ("'yes' is wrong answer ;(. Correct answer was 'no'.)")
            break
        else:
            print("Correct!")
            count += 1
    if count == 3:
        print(f"Congratulations, {name}!")

welcome_user()