from cs50 import get_float

while True:
    cents = get_float("Change: ")
    if cents > 0:
        break

cents = round(cents * 100)

coins = 0

# Number of Quarters
while cents >= 25:
    cents -= 25
    coins += 1

# Number of Dimes
while cents >= 10:
    cents -= 10
    coins += 1

# Number of Nickles
while cents >= 5:
    cents -= 5
    coins += 1

# Number of Pennies
while cents >= 1:
    cents -= 1
    coins += 1

print(coins)
