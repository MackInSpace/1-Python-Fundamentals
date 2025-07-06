def show_homepage():
    print("")
    print("       === DonateMe Homepage ===         ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register         |")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations   |")
    print("------------------------------------------")
    print("|              5.    Exit                  |")
    print("------------------------------------------")

def donate(username):
    while True:
        donation_amt = input("Enter amount to donate: ")

        try:
            amount = float(donation_amt)
            if amount <= 0:
                print("Donation amount must be greater than $0.")
            else:
                donation_string = f"{username} donated ${amount:.2f}"
                print("Thank you for your generosity!")
                return donation_string
        except ValueError:
            print("Please enter a valid numeric donation amount.")

def show_donations(donations):
    print("\n--- All Donations ---")
    if len(donations) == 0:
        print("Currently, there are no donations.")
    else:
        total = 0.0
        for donation in donations:
            print(donation)

        try: 
            amount = float(donation.split("$")[1])
            total += amount
        except (IndexError, ValueError):
            print("Could not parse donation amount.")

    print(f"\nTotal amount donated: ${total:.2f}")