import sys
# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt("Welcome to Calculator!")

prompt("What's the first number?")
number1 = input()

while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

prompt("What's the second number?")
number2 = input()

while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

prompt("What operation would you like to perform?\nEnter "
      '"1" for Add, "2" for Substract, "3" for Multiply, "4" for Divide')
operation = input()

operations = ['1', '2', '3', '4']
while operation not in operations:
    prompt("You must choose 1, 2, 3, or 4")
    operation = input()

match operation:
    case "1":
        output = int(number1) + int(number2)
    case "2":
        output = int(number1) - int(number2)
    case "3":
        output = int(number1) * int(number2)
    case "4":
        if int(number2) != 0:
            output = int(number1) / int(number2)
        else:
            sys.exit("Cannot divide by 0.")

prompt(f"The result is: {output}")
