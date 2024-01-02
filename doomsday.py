#!/usr/bin/python3

import sys
import random
from datetime import datetime, timedelta
import time


MAIN_MENU = """
Choose one of the following:
    1. Practice Mode
    2. Date Lookup
    3. Stats
    4. Quit
"""


def main():
    initial_choice = sys.argv[1] if len(sys.argv) > 1 else False

    while True:
        if initial_choice:
            choice = initial_choice
            initial_choice = False

        else:
            print(MAIN_MENU)
            choice = input("Your choice: ")
            print()

        if choice == "1" or "practice mode".startswith(choice.lower()):
            print()
            print("Enter q to return to main menu.")

            while True:
                print()

                random_date = get_random_date("1700-01-01", "2299-12-31")
                day_of_week = random_date.strftime("%A")

                begin_time = time.time()
                guess = input(f"What day of the week is {random_date.strftime('%B %-d, %Y')}? ")
                end_time = time.time()
                duration = round(end_time - begin_time, 2)

                if is_quit(guess):
                    break

                elif day_of_week.lower().startswith(guess.lower()):
                    print("Correct!")
                    print(f"You answered in {duration}s.")

                else:
                    print(f"Incorrect, it is a {random_date.strftime('%A')}.")


        elif choice == "2" or "date lookup".startswith(choice.lower()):
            print()
            print("Not implemented yet.")
            #  print("Enter q to return to main menu.")

        elif choice == "3" or "stats".startswith(choice.lower()):
            print()
            print("Not implemented yet.")
            #  print("Enter q to return to main menu.")

        elif choice == "4" or is_quit(choice):
            print("Goodbye!")
            break

        else:
            print()
            print(f"{choice} is not an option.")


def get_random_date(start_date, end_date):
    # thanks chatGPT
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    delta = end - start
    random_days = random.randint(0, delta.days)
    random_date = start + timedelta(days=random_days)
    return random_date


def is_quit(user_input):
    quit_words = ["exit", "quit", "done"]

    return any(word.startswith(user_input.lower()) for word in quit_words)


if __name__ == "__main__":
    main()
