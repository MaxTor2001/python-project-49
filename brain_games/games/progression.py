import random


def welcome_user():
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    count = 0
    while count < 3:
        while True:
            start = random.randint(0, 48)
            stop = random.randint(59, 99)
            step = random.randint(3, 10)
            numbers = list(range(start, stop, step))
            if len(numbers) >= 10:
                break
        
        hide_index = random.randint(0, len(numbers) - 1)
        hide1 = numbers[hide_index]
        hidden_numbers = []

        for i in range(start, stop, step):
            if i == hide1:
                hidden_numbers.append('..')
            else:
                hidden_numbers.append(str(i))

        result = ' '.join(hidden_numbers)
        
        while True:
            prompt = (
                "What number is missing in the progression?\n"
                f"Question: {result} \n"
                "Your answer: "
            )
            try:
                user_answer = float(input(prompt))
                break
            except ValueError:
                print('Incorrect input. Please enter "numbers".')
        if abs(user_answer - hide1) == 0:
            print("Correct!")
            count += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer is '{hide1}'."
            )
            print(f"Let's try again, {name}!")
            break

    if count == 3:
        print(f"Congratulations, {name}!")


welcome_user()
