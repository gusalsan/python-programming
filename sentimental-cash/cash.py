# Ask for change
while True:
    try:
        change = float(input("Change owed: "))
        break
    except ValueError:
        print("The change must be a float")
        change = float(input("Change owed: "))

# Change must be greater than 0
while change < 0:
    change = float(input("Change owed: "))

# Define coins and calculate the number of coins for change
coins = 0

while change >= 0.25:

    change = round(change - 0.25, 2)
    print(change)
    coins += 1

while change >= 0.10:
    change = round(change - 0.10, 2)
    print(change)
    coins += 1

while change >= 0.05:
    print(change)
    change = round(change - 0.05, 2)
    print(change)
    coins += 1

while change >= 0.01:
    change = round(change - 0.01, 2)
    print(change)
    coins += 1

# Print the number of coins
print(coins)
