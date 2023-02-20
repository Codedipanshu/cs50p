def main():
    frac = input("Fraction: ")
    percent = convert(frac)
    print(gauge(percent))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            a = int(x)
            b = int(y)
            f = a / b
            if f <= 1:
                return int(f * 100)
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()

