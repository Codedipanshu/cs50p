list = {}

while True:
    try:
        item = input().lower()
        if not item in list:
            list[item] = 1
        else:
            list[item] += 1
    except EOFError:
        for item in sorted(list.keys()):
            print(list[item], item.upper())
        break
    except KeyError:
        pass