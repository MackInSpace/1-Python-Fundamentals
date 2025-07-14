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
        print("Bob has an account balance of:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

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