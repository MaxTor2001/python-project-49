import prompt


#text=f'''Welcome to the Brain Games!
#Hello, {name}'''



def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I Have your name?')
    print(f'''Hello, {name}''')

def main():
    greet()

if __name__ == "__main__":
    main()

