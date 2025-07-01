import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user = input("Press enter to pick a card or type 'Q' to quit: ")
    if user == "Q":
        break
    else:
        card = random.choice(diamonds)
        hand.append(card)
        diamonds.remove(card)
        print("Your hand is: ", hand)
        print("There are", len(diamonds), "cards left.")
        print("Remaining cards: ", diamonds)

    if not diamonds:
        print("There are no more cards left.")