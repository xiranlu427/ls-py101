"""
A car loan calculator that calculates the monthly payment based on three user
inputs: the loan amount in dollars, the APR, and the loan duration in years
and months.
"""

import json

with open('loan_calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    """Format and display interactive messages."""
    print(f"==> {message}")


def invalid_number(number_str):
    """Validate the numeric input and catch potential errors. Return bool:
    True if input is invalid, False if valid."""
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError("Value must be greater than 0: {number_str}")
    except ValueError:
        return True
    return False


def invalid_duration(duration_inputs):
    """Validate the duration input and catch potential errors. Return bool:
    True if input is invalid, False if valid."""
    if not 1 <= len(duration_inputs) <= 2:
        return True

    if len(duration_inputs) == 1:
        try:
            num = int(duration_inputs[0])
            if num <= 0:
                raise ValueError(f"Value must > 0: {num}")
        except ValueError:
            return True
        return False

    try:
        num1 = int(duration_inputs[0])
        num2 = int(duration_inputs[1])
        if num1 == 0 and num2 == 0:
            raise ValueError(f"Expect at least one positive value"
                        f": {duration_inputs}")
    except ValueError:
        return True
    return False


def get_valid_num_input(msg, error_msg):
    """Prompt the user for a valid numeric value. Return float:
    numeric input."""
    prompt(MESSAGES[msg])
    number_str = input()

    while invalid_number(number_str):
        prompt(MESSAGES[error_msg])
        number_str = input()

    return float(number_str)


def is_whole_years(duration_inputs):
    """Check if the loan duration is whole years. Return bool: True if
    duration is whole years, False if not."""
    return len(duration_inputs) == 1


def get_valid_duration(msg, error_msg):
    """Prompt the user for a valid duration input in years (and months).
    Return integer: number of months."""
    prompt(MESSAGES[msg])
    duration_inputs = input().split()

    while invalid_duration(duration_inputs):
        prompt(MESSAGES[error_msg])
        duration_inputs = input().split()

    years = int(duration_inputs[0])
    duration_in_months = years * 12

    if not is_whole_years(duration_inputs):
        months = int(duration_inputs[1])
        duration_in_months += months

    return duration_in_months


def calculate_monthly_payment(loan_amount, apr, duration_in_months):
    """Calculate the monthly payment based on the loan amount, apr,
    and loan duration. Return float: monthly payment."""
    monthly_interest_rate = apr / 12
    monthly_payment = loan_amount * (monthly_interest_rate /
            (1 - (1 + monthly_interest_rate) ** (-duration_in_months)))
    return monthly_payment


def display_result(payment, duration, interest):
    """Format and display the result."""
    print("==========================================")
    print(MESSAGES["result"].format(output = payment, duration = duration,
                                     interest = interest * 100))
    print("==========================================")


def get_valid_yn_answer(answer_str):
    """Prompt the user for a valid y/n answer. Return bool: True if input
    is 'yes', False if 'no'."""
    while True:
        if answer_str and (answer_str[0] == 'n' or answer_str[0] == 'y'):
            break

        prompt(MESSAGES["invalid_answer"])
        answer_str = input().lower()

    return answer_str[0] == 'y'


def perform_another_calc():
    """Check if the user wants another calculation and validate the user input.
    Return bool: True if 'yes' to another calculation, False if 'no'."""
    prompt(MESSAGES["another_calculation"])
    answer_str = input().lower()
    try_again = get_valid_yn_answer(answer_str)
    return try_again


def main():
    """Calculate the monthly payment based on three user inputs: the loan 
    amount in dollars, the APR, and the loan duration in years (and months)."""
    prompt(MESSAGES["welcome"])
    while True:
        loan_amount = get_valid_num_input("amount_prompt", "invalid_number")
        annual_interest_rate = (
        get_valid_num_input("interest_prompt", "invalid_number") / 100)
        duration_in_months = (
        get_valid_duration("duration_prompt", "invalid_duration"))
        monthly_payment = calculate_monthly_payment(loan_amount,
                        annual_interest_rate, duration_in_months)
        display_result(monthly_payment, duration_in_months,
                        annual_interest_rate)

        if not perform_another_calc():
            break


main()