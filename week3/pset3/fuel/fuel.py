def main():
    frac = con_int()
    x, y = frac.split("/")
    print_result(int(x), int(y))


def con_int():
    while True:
        try:
            frac = input("Fraction: ")
            x, y = frac.split("/")
            f = int(x) / int(y)
            if f <= 1:
                return frac
        except (ValueError, ZeroDivisionError):
            pass


def print_result(a, b):
    result = a / b *100
    if result <= 1:
        print("E")
    elif result >= 99:
        print("F")
    else:
        print(f"{result:.0f}%")



main()