from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
authorized_user = ""
show_homepage()

if authorized_user == "":
    print("You must be logged in to donate.")
else:
    print(f"Logged in as {authorized_user}")

while True:
    choice = input("Choose an option: ")

    if choice == "1":
        username = input("\nEnter your username: ")
        password = input("Enter your password: ")
        authorized_user = login(database, username, password)
    elif choice == "2":
        username = input("\nEnter your username: ")
        password = input("Enter your password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password
    elif choice == "3":
        if authorized_user == "":
            print("\nYou are not logged in.")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
    elif choice == "4":
        show_donations(donations)
    elif choice == "5":
        print("Leaving DonateMe...")
        break
    else: 
        print("Invalid option. Please choose a valid number from the menu.")

    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as {authorized_user}")