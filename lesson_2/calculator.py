import sys
# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

print("Welcome to Calculator!")


number1 = int(input("What's the first number?\n"))
number2 = int(input("What's the second number?\n"))

print("What operation would you like to perform?\nEnter " 
      '"1" for Add, "2" for Substract, "3" for Multiply, "4" for Divide')

operation = input()

match operation:
    case "1":
        output = number1 + number2
    case "2":
        output = number1 - number2
    case "3":
        output = number1 * number2
    case "4":
        if number2 != 0:
            output = number1 / number2
        else:
            sys.exit("Cannot divide by 0.")
    case _:
        sys.exit("Invaid operation.")
      
print(f"The result is: {output}")