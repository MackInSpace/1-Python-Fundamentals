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

"""
Addition
"""
x = 1
y = 2 
z = 3
xyz = x + y + z # xyz = 1 + 2 + 3 = 6
x = x + 10 # x = 1 + 10 11
y = y + 7 # y = 2 + 7 = 9
z = z + 9 # z = 3 + 9 = 12

"""
Subtraction
"""
x = 10
y = 2
z = 3
xyz = x - y - z # xyz = 10 - 2 - 3 = 5
x = x - 10 # x = 10 - 10 = 0
y = y - 7 # y = 2 - 7 = -5
z = z - 9 # z = 3 - 9 = -6

"""
Multiplication
"""
x = 1
y = 2
z = 3
xyz = x * y * z # xyz = 1 * 2 * 3 = 6
x = x * 10 # x = 10 * 10 = 10
y = y * 7 # y = 2 * 7 = 14
z = z * 9 # z = 3 * 9 = 27

"""
Division
"""
x = 20
y = 5
z = 4
xyz = x / y / z # xyz = 20 / 5 / 4 = 1.0 (float value)
x = x / 10 # x = 20 / 10 = 2.0
y = y / 5 # y = 5 / 5 = 1.0
z = z / 3 # z = 4 / 3 = 1.3

"""
Floor Division
"""
x = 20
y = 5
z = 4
xyz = x // y // z # xyz = 20 // 5 // 4 = 1 (integer value)
x = x // 10 # x = 20 // 10 = 2
y = y // 5 # y = 5 // 5 = 1
z = z // 3 # z = 4 // 3 = 1

"""
Exponentiation
"""
x = 2 ** 0 # 1
y = 2 ** 1 # 2
z = 2 ** 2.0 # 4.0

"""
Modulo
"""
x = 23
y = 5
z = 2 % 2 # 0
xy = x % 5 # 23 % 5 = 3
xx = 2 % 23 # 2 % 23 = 2

#Remember PEMDAS for all math operations 'Please Excuse My Dear Aunt Sally', work form left to right

"""
Python Comparison Operators
"""
X = 100
Y = 200

print( X != Y ) # True
print( X > Y ) # False
print( X < Y ) # True
print( X >= Y ) # False
print( X <= Y ) # True

"""
Logical Operators
"""
X = 100
Y = 200
Z = 100

print( X < Y and Y > Z ) # True
print( X > Y or Y > Z ) # True
print(not(X > Y or Y > Z)) # False

"""
Multi-line Code Blocks
"""
#if weather == "cold":
#    print("It's cold outside")
#    print("Wear a jacket")
#else:
#    print("It's warm outside")
#    print("Wear shorts")

"""
Chained Conditionals
"""
if x < 2:
    print("small")
elif x < 10:
    print("medium")
else:
    print("large")

"""
Nested Conditions
"""
if x > 1 and x < 100:
    print("More than one")
    print("Less than 100")
print("Finished")