import random

def guess_random_number(tries, start, stop):
    target = random.randint(start, stop)
    guessed = set()

    while tries != 0:
        print(f"Number of tries left: {tries}")
        try:
            guess = int(input(f"Guess a random number between {start} and {stop}: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess < start or guess > stop:
            print("Out of range.")
            continue
        if guess in guessed:
            print("You have already guessed this number.")
            continue

        guessed.add(guess)

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

""" if __name__ == "__main__":
    guess_random_num_linear(5, 0, 10) """

def guess_random_num_binary(tries, start, stop):
    target = random.randint(start, stop)
    print(f"Random number to find: {target}")

    low = start
    high = stop

    while tries > 0 and low <= high:
        guess = (low + high) // 2
        print(f"Guessing... {guess}")
        tries -= 1

        if guess == target:
            print(f"Found it! {target}")
            return
        elif guess < target:
            print("Guessing higher!")
            start = guess + 1
        else:
            print("Guessing lower!")
            stop = guess - 1

    print(f"Your program failed to find the number.")

if __name__ == "__main__":
    guess_random_num_binary(5, 0, 100)

def run_game():
    try:
        tries = int(input("Enter number of tries: "))
        start = int(input("Enter start of range: "))
        stop = int(input("Enter end of range: "))
    except ValueError:
        print("Invalid input.")
        return

    print("Choose mode:")
    print("1. You guess")
    print("2. Linear search")
    print("3. Binary search")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        guess_random_number(tries, start, stop)
    elif choice == "2":
        guess_random_num_linear(tries, start, stop)
    elif choice == "3":
        guess_random_num_binary(tries, start, stop)
    else:
        print("Invalid choice.")