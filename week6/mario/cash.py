while True:
    try:
        cents = float(input("Change owed: "))
        if cents >= 0:
            cents = round(cents * 100)
            break
    except ValueError:
        continue

count = 0

count += cents // 25
cents %= 25

count += cents // 10
cents %= 10

count += cents // 5
cents %= 5

count += cents
cents = 0

print(int(count))
