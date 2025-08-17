# Variables and Data Types
# int
age = 21
print("Age:", age, "| Type:", type(age))
# float
pi = 3.14
print("Pi:", pi, "| Type:", type(pi))
# string
name = "Sam"
print("Name:", name, "| Type:", type(name))
# boolean
is_student = True
print("Is Student:", is_student, "| Type:", type(is_student))
#----------------------------------------------------------------
# operator
a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.333...
print(a % b)  # 1  (remainder)
print(a ** b) # 1000 (power: 10^3)
print(a // b) # 3 (floor division)
#------------------------------------------------------------------
#if-else Statements
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#loops
#for loop
for i in range(1, 6):
    print(i)  # prints 1 to 5
#while loop
i = 1
while i <= 5:
    print(i)
    i += 1
#----------------------------------------------------------------
# Calculator Program
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result =", a + b)
elif op == "-":
    print("Result =", a - b)
elif op == "*":
    print("Result =", a * b)
elif op == "/":
    print("Result =", a / b)
else:
    print("Invalid operator")

#----------------------------------------------------------------
# Even/Odd Checker
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#---------------------------------------------------------------
# Multiplication Table Generator
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)