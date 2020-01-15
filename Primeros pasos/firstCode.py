# Project basic commands :)

# Numeric or text create automatically depends of the type
number = 10  # print(type(number)) report type int
number = 10.56  # print(type(number)) report type float
chain = "Hola hola !!!"  # print(type(chain)) report type string
value = True  # print(type(value)) report type Boolean

# Dynamic typing : change the type of value in the same variable
number = "now I'm a String!"
# print(number)

'''Comment
    multi
    linea'''

# Examples of operations
n1 = 10
n2 = 3
sum_ = n1 + n2
remainder_ = n1 - n2
multiplication_ = n1 * n2
division_ = n1 / n2
division_to_down = n1 // n2
module_ = n1 % n2
potency_ = n1 ** n2
nT = (n1 + n2) * 18 / 2
exNumber = 3 ** 3 * (13 / 5 - (2 * 4))
# print("The answer is ", nT)

# Relational operations : return boolean answers
# <, >, =, <=, >=, !=, ==
result = 10 == 20
# print(nT >= exNumber)
# print(result)

# Logical operations: and / or / not
# evaluation order --> not -> and -> or
a = 10
b = 12
c = 13
d = 10
# print(((a > b) or (a < c)) and ((a == c) or (a >= b)))
#        F           T              F            F
#               T                        F

''' Priority of operations:
    1. ()
    2. **
    3. *, /, mod, not
    4. +, -, and
    5. <, >, ==, >=, <=, !=, or
'''
b = 15
c = 20
result = not ((a < b) and (b < c))
# print(result)

# Assign operations
a = 0
a += 5  # sum in assignment
a -= 2  # subtraction in assignment
a *= 3  # multiplication in assignment
a /= 3  # Division in assignment
a **= 2  # Potency in assignment
a %= 2  # module in assignment

# Output by console
by = "Tati"
created = "January"
# print("Python course by {} created in {}".format(by, created))
# print(f"Python course by {by} created in {created}")

# Incoming of data
# name = input("Write your name: ")  # String
# number = int(input("Write a number"))  # Int
# float_ = float(input("now a number with . ")) # float

# Integrated functions
n = str(number)  # become to string
n = bin(10)  # become to binary
n = int("0b1010", 2)  # binary to int
n = int("0xa", 16)  # hexadecimal to int
n = abs(-8)  # Absolute value
n = round(5.6)  # Round the number
n = len("Tati")  # count the number of characters
# print(n)


