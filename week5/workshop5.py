import random

def guess_random_number(tries, start, stop):
    target = random.randint(start, stop)

    while tries != 0:
        print(f"Number of tries left: {tries}")
        guess = int(input(f"Guess a random number between {start} and {stop}: "))

        if guess == target:
            print("You guessed the correct number!")
            return
        elif guess < target:
            print("Guess higher!")
        else:
            print("Guess lower!")

        tries -= 1

    print(f"You have failed to guess the number: {target}.")

""" if __name__ == "__main__":
    guess_random_number(5, 0, 10) """

def guess_random_num_linear(tries, start, stop):
    target = random.randint(start, stop)
    print(f"The number for the program to guess is: {target}")

    for guess in range(start, stop + 1):
        if tries == 0:
            break
        
        print(f"Number of tries left: {tries}")
        print(f"The program is guessing... {guess}")
        tries -= 1

        if guess == target:
            print(f"The program has guessed the correct number!")
            return
        
    print(f"The program has failed to guess the correct number.")

if __name__ == "__main__":
    guess_random_num_linear(5, 0, 10)