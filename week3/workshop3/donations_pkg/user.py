def login(database, username, password):
    username_lower = username.lower()
    if len(username) > 10:
        print("\nUsername must be 10 characters or less.")
        return ""
    if len(password) < 5:
        print("\nPassword must be 5 characters or more.")
        return ""
    if username_lower in database:
        if database[username_lower] == password:
            print("\nWelcome back admin!")
            return username_lower
        else: 
            print("Incorrect password for admin.")
            return ""
    else:
        print("\nUser not found. Please register.")
        return ""
    
def register(database, username):
    username_lower = username.lower()
    if username_lower in database:
        print("\nUser already registered.")
        return ""
    else:
        print(f"\nUsername {username} registered!")
        return username_lower