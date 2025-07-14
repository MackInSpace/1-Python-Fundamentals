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


""" Driver Code for Task 1 """
# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)

""" Driver Code for Task 2 """
user2 = User("Bob", 1234, "password")
print(user2.name, user2.pin, user2.password)

user2.change_name("Bobby")
user2.change_pin(4321)
user2.change_password("newpassword")

print(user2.name, user2.pin, user2.password)