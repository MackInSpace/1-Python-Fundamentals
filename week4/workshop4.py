class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name + " has an account balance of:", self.balance)

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal failed: Enter a valid positive number")
            return False
        if amount > self.balance: 
            print("Withdrawal failed: Insufficient funds")
            return False
        self.balance -= amount
        print(f"${amount} withdrawn from {self.name}'s account. New balance: ${self.balance}")
        return True

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Deposit failed: Enter a valid positive number")
            return False
        self.balance += amount
        print(f"${amount} deposited into {self.name}'s account. New balance: ${self.balance}")
        return True

    def transfer_money(self, amount, recipient):
        print("\nYou are transferring $" + str(amount) + " to " + recipient.name)
        print("Authentication required")
        entered_pin = int(input("Enter your PIN: "))
        if entered_pin == self.pin:
            if self.balance >= amount:
                self.balance -= amount
                recipient.balance += amount
                print("Transfer authorized")
                print("Transferring $" + str(amount) + " to " + recipient.name)
                return True
            else: 
                print("Invalid PIN. Transaction canceled.")
                print("Alice has an account balance of:", self.balance)
                print("Bob has an account balance of:", recipient.balance)
                return False
        else:
            print("Invalid PIN. Transaction canceled.")
            print("Alice has an account balance of:", self.balance)
            print("Bob has an account balance of:", recipient.balance)
            return False
        
          
    def request_money(self, amount, recipient):
        print(f"\nYou are requesting ${amount} from {recipient.name}")
        print("User authentication required...")
        entered_pin = int(input("Enter " + recipient.name + "'s PIN: "))
        if entered_pin == recipient.pin:
            entered_password = input(f"Enter your password: ")
            if entered_password == recipient.password:
                print("Request authorized")
                print("Transferring funds...")
                self.balance += amount
                recipient.balance -= amount
                print(recipient.name + " has received $" + str(amount))
                return True
            else: 
                print("Invalid password. Transaction canceled.")
                print("Alice has an account balance of:", self.balance)
                print("Bob has an account balance of:", recipient.balance)
                return False
        else:
            print("Invalid PIN. Transaction canceled.")
            print("Alice has an account balance of:", self.balance)
            print("Bob has an account balance of:", recipient.balance)
            return False


user2 = BankUser("Alice", 5678, "password")
user1 = BankUser("Bob", 1234, "password") 

user2.deposit(5000)
user2.show_balance()
user1.show_balance()

if user2.transfer_money(500, user1):
    user2.show_balance()
    user1.show_balance()

    if user2.request_money(250, user1):
        user2.show_balance()
        user1.show_balance()
    

""" Driver Code for Task 1 """
# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)

""" Driver Code for Task 2 """
# user2 = User("Bob", 1234, "password")
# print(user2.name, user2.pin, user2.password)

# user2.change_name("Bobby")
# user2.change_pin(4321)
# user2.change_password("newpassword")

# print(user2.name, user2.pin, user2.password)

""" Driver Code for Task 3 """
# user3 = BankUser("Bob", 1234, "password")
# print(user3.name, user3.pin, user3.password, user3.balance)

""" Driver Code for Task 4 """
# bank_user2 = BankUser("Bob", 1234, "password")
# bank_user2.show_balance()

# bank_user2.deposit(1000.0)
# bank_user2.show_balance()

# bank_user2.withdraw(500.0)
# bank_user2.show_balance()