import random
import sys

def main():
    level = get_positive_int("Level: ")

    result = random.randint(1, level)

    while True:
        guess = get_positive_int("Guess: ")

        if result > guess:
            print("Too small!")
        elif result < guess:
            print("Too large!")
        elif result == guess:
            sys.exit("Just right!")

def get_positive_int(prompt):
    while True:
        level = input(prompt)
        try:
            if 1 <= int(level):
                return int(level)
        except ValueError:
            pass

main()