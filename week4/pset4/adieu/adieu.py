import inflect

p = inflect.engine()

names = []
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print()
        break
list = p.join(names)
print(f"Adieu, adieu, to {list}")