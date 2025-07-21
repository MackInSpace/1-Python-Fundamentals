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

if __name__ == "__main__":
    guess_random_number(5, 0, 10)