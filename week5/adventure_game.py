import random

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