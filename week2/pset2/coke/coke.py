amount = 50

while True:
    print(f"Amount Due: {amount}")
    insert = int(input("Insert Coin: "))
    if insert in [25, 10, 5]:
        amount = amount - insert
        if amount < 1:
            print(f"Change Owed: {amount - amount * 2}")
            break
