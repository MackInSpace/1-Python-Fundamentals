def login(database, username, password):
    if username in database:
        if database[username] == password:
            print("\nWelcome back admin!")
            return username
        else: 
            print("Incorrect password for admin.")
            return ""
    else:
        print("\nUser not found. Please register.")
        return ""
    
def register(database, username):
    if username in database:
        print("\nUser already registered.")
        return ""
    else:
        print(f"\nUsername {username} registered!")
        return username