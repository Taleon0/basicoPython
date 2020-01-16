# Youtube Exercises

# Basic commands
# Exercise number 1
''' a = float(input("Write a value: "))
b = float(input("Write b value: "))
c = float(input("Write c value: "))
answer = (a**3 * (b**2 - 2*a*c))/(2*b)
print(f"The answer is : {answer}")'''
# Exercise number 2
"""
a = float(input("Write a value: "))
b = float(input("Write b value: "))
answer = ((3 + 5 * 8) < 3 and ((-6 / 3 * 4)+2 < 2)) or (a > b)
#               43 F                -6 T                   T/F
print(f"The answer is : {answer}")
"""
# Exercise number 3
'''a = float(input("Write a value: "))
b = float(input("Write b value: "))

# Exchange values
a, b = b, a
print(f"The new value of a is {a} and the new value of b is {b}")'''
# Exercise number 4
import math
'''radius = float(input("Insert the value of the radius: "))
area = math.pi * radius**2
cLength = 2 * math.pi * radius
print(f"The area of the circumference is {area:.2f} and the length is {cLength:.2f}")  # just two tenths after the point'''
# Exercise number 5
'''pValue = float(input("Insert purchase value: "))
percentage = pValue*0.15
tValue = pValue-percentage
print(f"The percentage is ${tValue:.2f}")'''

# Conditional
# Exercise 1
'''n1 = int(input("Insert a number, please: "))
n2 = int(input("Insert other number, please: "))

if n1 % 2 == 0 and n2 % 2 == 0:
    print("Both numbers are pair")
elif n1 % 2 == 0 and n2 % 2 != 0:
    print("First number is pair")
elif n1 % 2 != 0 and n2 % 2 == 0:
    print("Second number is pair")
else:
    print("Both numbers are odd")'''
# Exercise 2
'''n1 = int(input("Insert first number: "))
n2 = int(input("Insert second number: "))
n3 = int(input("Insert third number: "))

if n1 >= n2 and n1 >= n3 :
    print(f"The bigger number is: {n1}")
elif n2 >= n3 and n2 >= n1 :
    print(f"The bigger number is: {n2}")
elif n3 >= n1 and n3 >= n2 :
    print(f"The bigger number is: {n3}")
else:
    print("Invalid number")'''
# Exercise 3
'''sInput = input("Insert 1 character: ").lower()
sLong = len(sInput)

if sLong == 1:
    if sInput == "a" or sInput == "e" or sInput == "i" or sInput == "o" or sInput == "u":
        print("The character ir a vowel")
    else:
        print("The character is not a vowel")
elif sLong == 0:
    print("You used nothing")
else:
    print("You used more than 1 character")'''
# Exercise 4
# calculator
'''n1 = float(input("Insert number 1: "))
n2 = float(input("Insert number 2: "))
inputC = input("Insert a character depending of the operation: \n s for sum, r for subtraction, "
               "m  or p for multiplication or d for division ->").lower()
if inputC == "s":
    total = n1+n2
    print(f"The answer of sum is {total:.2f}")
elif inputC == "r":
    total = n1-n2
    print(f"The answer of subtraction is {total:.2f}")
elif inputC == "m" or inputC == "p":
    total = n1*n2
    print(f"The answer of multiplication is {total:.2f}")
elif inputC == "d":
    total = n1/n2
    print(f"The answer of division is {total:.2f}")
else:
    print("this is an invalid option")'''


