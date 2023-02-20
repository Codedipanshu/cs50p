def main():
    exp = input("Expression: ")

    x, y, z = exp.split(" ")
    result = eval(float(x), y, float(z))
    print(f"{result:.1f}")

def eval(a, b, c):
    if b == "+":
        return a + c
    elif b == "-":
        return a - c
    elif b == "*":
        return a * c
    else:
        return a / c

main()