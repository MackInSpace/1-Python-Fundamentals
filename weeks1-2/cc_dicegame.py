import random

high_score = 0


def dice_game():
    global high_score
    while True:
        print("Current High Score: ", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        break

    try: 
        player_choice = input("Enter a choice: ")
        
        if player_choice == "1":
            roll_1 = random.randint(1, 6)
            print("\nYou roll a... ", roll_1)
            roll_2 = random.randint(1, 6)
            print("You roll a... ", roll_2)
            roll_total = roll_1 + roll_2
            print("\nYou rolled a total of: ", roll_total)
            if roll_total > high_score:
                print("\nNew High Score!")
                print("\nCurrent High Score: ", roll_total)
            else:
                print()
        elif player_choice == "2":
            print("Thanks for playing!")

        else: 
            print("Please choose 1 or 2")

    except ValueError:
        print("Please enter a number")

dice_game()
