import sys
import json
# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False


while True:
    prompt(MESSAGES['welcome'])

    prompt(MESSAGES['number1_q'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES['invalid_number'])
        number1 = input()

    prompt(MESSAGES['number2_q'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES['invalid_number'])
        number2 = input()

    prompt(MESSAGES['operation_q'])
    operation = input()

    operations = ['1', '2', '3', '4']
    while operation not in operations:
        prompt(MESSAGES['invalid_operation'])
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            if float(number2) != 0:
                output = float(number1) / float(number2)
            else:
                sys.exit(prompt(MESSAGES['division_by_zero']))
    
    output = round(output, 2)
    prompt(MESSAGES['result'].format(output = output))
    prompt(MESSAGES['repeat_q'])
    answer = input()
    if answer and answer[0].lower() != 'y':
        break

