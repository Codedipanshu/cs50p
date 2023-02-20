original = input("Input: ")
print("Output: ", end="")

for c in original:
    if not c.lower() in ["a", "e", "i", "o", "u"]:
        print(c, end="")
print()