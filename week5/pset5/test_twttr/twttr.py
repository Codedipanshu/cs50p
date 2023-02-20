def main():
    original = input("Input: ")
    result = shorten(original)
    print("Output: " + result)


def shorten(word):
    new_word = ""
    for c in word:
        if not c.lower() in ["a", "e", "i", "o", "u"]:
            new_word += c
    return new_word


if __name__ == "__main__":
    main()
