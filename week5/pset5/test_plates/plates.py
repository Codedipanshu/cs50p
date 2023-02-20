def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and  s[0:2].isalpha() and s.isalnum():
        for c in s:
            if c.isdigit():
                index = s.index(c)
                if s[index:].isdigit() and c != "0":
                    return True
                else:
                    return False
        return True
    return False


if __name__ == "__main__":
    main()
