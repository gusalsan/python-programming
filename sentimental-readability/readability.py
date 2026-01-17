# Ask for text
text = input("Text: ")

# Calculate the number of letters in the text
letters = 0
for character in text:
    if character.isalpha():
        letters += 1

# print("The number of letters is :", letters)

# Calculate the number of words in the text.
separate_text = text.split()
words = len(separate_text)
# print("Number of words is: ", words)

# Calculate the number of sentences.
sentences = 0
for character in text:
    if character == ".":
        sentences += 1

    elif character == "?":
        sentences += 1

    elif character == "!":
        sentences += 1
# print("Number of sentences is: ", sentences)

# Colemans formula
letter_100_words = (letters/words) * 100
sentences_100_words = (sentences/words) * 100
formula = (0.0588 * letter_100_words) - (0.296 * sentences_100_words) - 15.8
# print("The value of formula is: ", formula)

round_formula = round(formula)
# print(round_formula)

if round_formula < 1:
    print("Before Grade 1")
elif round_formula >= 16:
    print("Grade 16+")
else:
    print("Grade", round_formula)
