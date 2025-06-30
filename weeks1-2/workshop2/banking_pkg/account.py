def show_balance(balance):
    print("Your current balance is $" + str(balance))

def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return balance + float(amount)

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds. Withdrawal canceled.")
        return balance
    else:
        return balance - amount

def logout(name):
    print("Goodbye " + name + "!")