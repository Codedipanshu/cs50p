import random


def main():
    level = get_level()
    score = 0
    for q in range(10):
        trials = 0
        x = generate_integer(level)
        y = generate_integer(level)

        while True:
            solution = str(x + y)
            user_result = input(f"{x} + {y} = ")
            if user_result == solution:
                score += 1
                break
            elif user_result != solution and trials != 2:
                print("EEE")
                trials += 1
                continue
            else:
                print("EEE")
                print(f"{x} + {y} = {solution}")
                break

    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return level


def generate_integer(level):
    if level == "1":
        return random.randint(0, 9)
    elif level == "2":
        return random.randint(10, 99)
    elif level == "3":
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()