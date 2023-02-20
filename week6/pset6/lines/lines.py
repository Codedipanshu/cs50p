import sys

count = 0

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    try:
        with open(sys.argv[1]) as file:
            for old_line in file:
                line = old_line.lstrip()
                if line.startswith("#"):
                    count += 0
                elif old_line.isspace():
                    count += 0
                else:
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

print(count)