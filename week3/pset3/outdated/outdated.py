months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    if "/" in date:
        month, day, year = date.split("/")
    elif "," in date:
        date = date.replace(",", "")
        month, day, year = date.split(" ")
        if month in months:
            month = months.index(month) + 1
    try:
        if int(month) > 12 or int(day) > 31:
            continue
        elif " " in year:
            continue
        else:
            break
    except:
        continue
print(f"{year}-{int(month):02}-{int(day):02}")




















"""
while True:
    before = input("Date: ")
    try:
        m, d, y = before.split("/")
        if (1 <= int(m) <= 12) and (1 <= int(d) <= 31):
            break
    except:
        try:
            m, d, y = before.split(" ")
            for i in range(len(months)):
                if m == months[i]:
                    m = i + 1
                d = d.replace(",","")
            if (1 <= int(m) <= 12) and (1 <= int(d) <= 31):
                break
        except:
            print()
            pass
print(f"{y}-{int(m):02}-{int(d):02}")
"""