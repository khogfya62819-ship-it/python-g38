#

a=2
b=3

#def add(x,y)->int:
#    return x+y


def message():
    print("Welcome to the CLI Calculator!")

message()

number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = int(number1) + int(number2)
elif operation == "-":
    result = int(number1) - int(number2)
elif operation == "*":
    result = int(number1) * int(number2)
elif operation == "/":
    if int(number2) != 0:
        result = int(number1) / int(number2)
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"

print("Result:", result)
    