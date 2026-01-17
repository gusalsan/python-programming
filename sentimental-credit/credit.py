# Ask the number of credit card
card = int(input("Number: "))

# Access the digits on the card
first = int(str(card)[0])
two_first_digits = int(str(card)[:2])

# Make Luhn's algorithm
str_card = str(card)
str_card = str_card[::-1]
sum_even = 0
sum_odd = 0
for i in range(1, len(str_card), 2):
    number = int(str_card[i])
    first_step = (number*2)
    if first_step > 9:
        str_first_step = str(first_step)
        for digit in str_first_step:
            sum_even += int(digit)
    else:
        sum_even += first_step

for i in range(0, len(str_card), 2):
    number_odd = int(str_card[i])
    sum_odd += number_odd

comprobation = sum_even + sum_odd
print("Comprobation", comprobation)
str_comprobation = str(comprobation)
last_digit_comprobation = int(str_comprobation[-1])

# Implement the logic for know the type of card
if len(str_card) < 13:
    print("INVALID\n")

elif two_first_digits == 34 or two_first_digits == 37:
    print("AMEX\n")

elif last_digit_comprobation == 0:
    if first == 4:
        print("VISA\n")

    elif 50 < two_first_digits < 56:
        print("MASTERCARD\n")

    else:
        print("INVALID\n")

else:
    print("INVALID\n")
