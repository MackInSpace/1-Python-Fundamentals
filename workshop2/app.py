from banking_pkg import account 

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("    === Automated Teller Machine ===    ")

while True:
    name = input("Enter name to register: ")
    if 1 <= len(name) >= 10:
        break
    else:
        print("Invalid name. Please use 1 to 10 characters.")

while True:
    pin = input("Enter PIN: ")
    if len(pin) == 4:
        break
    else:
        print("Invalid PIN. Please use 4 digits.")
balance = 0

print(name + " has been registered with a starting balance of $" + str(balance))

while True:
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")

    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid Credentials!")

while True: 
    atm_menu(name)
    option = input("Choose an option:  ")

    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == "4":
        account.logout(name)
        break
    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")