from donations_pkg.homepage import show_homepage

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
        print("TODO: Write Login Functionality")
    elif choice == "2":
        print("TODO: Write Register Functionality")
    elif choice == "3":
        print("TODO: Write Donate Functionality")
    elif choice == "4":
        print("TODO: Write Show Donations Functionality")
    elif choice == "5":
        print("Leaving DonateMe...")
        break
    else: 
        print("Invalid option. Please choose a valid number from the menu.")

    print("\n")
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as {authorized_user}")