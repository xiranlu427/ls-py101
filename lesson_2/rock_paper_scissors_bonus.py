"""
An extended version of the classic Rock Paper Scissors game that includes two
additional options: Spock and Lizard. The user will play against the computer,
and the first player that reaches three wins becomes the grand winner.
"""

import random
import json
import os

with open('rock_paper_scissors_bonus_messages.json', 'r') as file:
    MESSAGES = json.load(file)

OPTIONS = {
    'r': "rock",
    'p': "paper",
    'sc': "scissors",
    'l': "lizard",
    'sp': "spock",
}

WIN_LOSS_PAIRS = {
    "rock":     ["scissors", "lizard"],
    "paper":    ["rock",     "spock"],
    "scissors": ["paper",    "lizard"],
    "spock":    ["rock",     "scissors"],
    "lizard":   ["paper",    "spock"],
}

MAX_SCORE = 3

def prompt(message):
    """Format and display the interactive message."""
    print(f"==> {message}")

def get_valid_user_choice():
    """Prompt the user for a valid choice and convert the abbreviated term
    to the full term. Return string: user_choice."""
    options = ', '.join(OPTIONS.values())
    prompt(MESSAGES["prompt_user_choice"].format(options = options))
    prompt(MESSAGES["prompt_instruction"])
    user_input = input().strip().lower()

    while matched_choice(user_input) is None:
        prompt(MESSAGES["invalid_choice"])
        user_input = input().strip().lower()

    user_choice = matched_choice(user_input)

    return user_choice

def matched_choice(string):
    """Match the (abbreviated) user input against the OPTIONS dictionary.
    Return string: a valid user choice, or None if input is invalid."""
    match string:
        case 'r' | "rock":
            return OPTIONS['r']
        case 'p' | "paper":
            return OPTIONS['p']
        case 'sc' | "scissors":
            return OPTIONS['sc']
        case 'sp' | "spock":
            return OPTIONS['sp']
        case 'l' | "lizard":
            return OPTIONS['l']
        case _:
            return None

def player1_wins(player1_choice, player2_choice):
    """Take in the choices of two players and return boolean: True if the
    first player wins, False if not."""
    return player2_choice in WIN_LOSS_PAIRS[player1_choice]

def display_round_winner(winner):
    """Display the winner or announce a tie."""
    if winner == "user":
        prompt(MESSAGES["user_wins"])
    elif winner == "computer":
        prompt(MESSAGES["computer_wins"])
    else:
        prompt(MESSAGES["tie"])

def display_game_score(user_score, computer_score):
    """Display the score for each round. If one player reaches three wins,
    announce the final winner and end game."""
    if user_score > computer_score:
        prompt(MESSAGES["user_leads"].format(
            user_score = user_score, computer_score = computer_score))
    elif user_score < computer_score:
        prompt(MESSAGES["computer_leads"].format(
            computer_score = computer_score, user_score = user_score))
    else:
        prompt(MESSAGES["draw"].format(
            user_score = user_score, computer_score = computer_score))

def display_game_winner(user_score, computer_score):
    if user_score > computer_score:
        prompt(MESSAGES["user_winner"].format(
        user_score = user_score, computer_score = computer_score))
    else:
        prompt(MESSAGES["computer_winner"].format(
        computer_score = computer_score, user_score = user_score))

def get_valid_yn_answer(answer):
    """Prompt the user for a valid y/n answer. Return bool: True if input
    is 'yes', False if input is 'no'."""
    while True:
        valid_answers = ['y', 'n', "yes", "no"]
        if answer in valid_answers:
            break
        prompt(MESSAGES["invalid_yn_answer"])
        answer = input().strip().lower()

    return answer[0] == 'y'

def get_consent_to_play_again():
    """Check if the user wants another game and validate the user input.
    Return bool: True if 'yes' to another game, False if 'no'."""
    prompt(MESSAGES["prompt_play_again"])
    answer = input().strip().lower()
    play_again = get_valid_yn_answer(answer)
    return play_again

def main():
    """Run the game Rock Paper Scissors Spock Lizard and prompt the user for
    moves against the computer."""
    keep_playing = True

    prompt(MESSAGES["welcome"])
    prompt(MESSAGES["intro"])

    while keep_playing:
        round_num, user_score, computer_score = 0, 0, 0
        winner = None

        while user_score != MAX_SCORE and computer_score != MAX_SCORE:
            round_num += 1
            print(MESSAGES["round"].format(round_num = round_num))
            user_choice = get_valid_user_choice()
            computer_choice = random.choice(list(OPTIONS.values()))
            prompt(MESSAGES["display_choices"].format(
                user_choice = user_choice, computer_choice = computer_choice))

            if player1_wins(user_choice, computer_choice):
                winner = "user"
                user_score += 1
            elif player1_wins(computer_choice, user_choice):
                winner = "computer"
                computer_score += 1
            else:
                winner = None

            display_round_winner(winner)

            if user_score == 3 or computer_score == 3:
                break
            display_game_score(user_score, computer_score)
        
        display_game_winner(user_score, computer_score)

        if not get_consent_to_play_again():
            keep_playing = False
            prompt(MESSAGES["end_game"])

        os.system('clear')

main()
