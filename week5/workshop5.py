import random

def guess_random_number(tries, start, stop):
    target = random.randint(start, stop)

    while tries != 0:
        print(f"Tries remaining: {tries}")
        guess = int(input(f"Guess a random number between {start} and {stop}: "))

        if guess == target:
            print("Congratulations! You guessed the correct number!")
            return
        elif guess < target:
            print("Guess higher!")
        else:
            print("Guess lower!")

        tries -= 1

    print(f"Sorry, you ran out of tries. The correct number was {target}.")