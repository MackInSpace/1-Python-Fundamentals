print("Hello World")

"""
Declaring Variables
"""
x = 12.2
y = 7
z = 9.0
print(x)
print(y)
print(z)

"""
Primitive Data Types
"""
name = "Bob" # String
age = 25 # Integer
cash = 100.25 # Float
retired = False # Boolean

#How to know the Date Type of a Variable
# Invoking the function 'type(<VARIABLE NAME>)'
print("Data Type of the variable 'name' is", type(name))
print("Data Type of the variable 'age' is", type(age))
print("Data Type of the variable 'cash' is", type(cash))
print("Data Type of the variable 'retired' is", type(retired))

"""
Composite Data Types
"""
nucamp_locations = ["Seattle", "Tacoma", "Bellevue"] #Storing a list
Bob_Info = {"name": "Bob", "age": 25, "cash": 100.25, "retired": False} #Storing a dictionary
my_tuple = ("apple", "banana", "cherry") #Storing a tuple
my_set = {"cats", "dogs", "birds"} #Storing a set

print("Data Type of the variable 'nucamp_locations' is", type(nucamp_locations))
print("Data Type of the variable 'Bob_Info' is", type(Bob_Info))
print("Data Type of the variable 'my_tuple' is", type(my_tuple))
print("Data Type of the variable 'my_set' is", type(my_set))