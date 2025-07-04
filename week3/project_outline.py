""" Initialize game: welcome message and instructions
Set up dictionary of rooms and paths
Set player stats: score = 0, inventory = [], game_over = False
While not game_over:
    Show current room and options
    Get player input
    Check if input is valid
    Update inventory or score based on choices
    Move player to next room
    Trigger puzzle if needed (e.g., “solve this loop”)
    Check win or loss conditions
End game with summary and replay option """

""" Key Python Data Structure: 
dict - Store rooms and branching paths
list - Manage inventory or event
set - Keep unique items like badges or rare items
int - Track scores
tuple - Store immutable settings or coordinates """