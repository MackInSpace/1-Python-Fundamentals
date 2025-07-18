import random

# Game setup
def welcome():
    print("🎮 Welcome to the Text Adventure Game!")
    print("Explore rooms, collect items, and solve puzzles to win.")
    print("Type commands like 'go north', 'take key', 'solve puzzle', or 'sort inventory'.")

rooms = {
    "entrance": {
        "description": "You are at the entrance of a mysterious cave.",
        "paths": {"north:": "hallway"},
        "items": [],
    },
    "hallway": {
        "description": "A dimly lit hallway with strange markings.",
        "paths": {"south": "entrance", "east": "chamber"},
        "items": ["torch"],
    },
    "chamber": {
        "description": "A large chamber with a puzzle pedestal.",
        "paths": {"west": "hallway"},
        "items": [],
        "puzzle": True,
    }
}

# Player state
score = 0
inventory = []
badges = set
current_room = "entrance"
game_over = False

def solve_loop_puzzle():
    print("🧩 Puzzle: What does this python code print?")
    print("x = [1,2,3]\nfor i in range(len(x)):\n  x[i] += 1\nprint(x)")
    answer = input("Your answer (enter the list result): ").strip()
    if answer == "[2, 3, 4]":
        print("🎉 Correct! +10 points and 'Logic Badge' earned.")
        return 10, "Logic Badge"
    else:
        print("❌ Incorrect. The correct answer is [2, 3, 4].")
        return 0, None
    
# Bubble Sort inventory
def bubble_sort_inventory(inv):
    sorted_inv = inv.copy()
    n = len(sorted_inv)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_inv[j] > sorted_inv[j + 1]:
                sorted_inv[j], sorted_inv[j + 1] = sorted_inv[j + 1], sorted_inv[j]
    return sorted_inv