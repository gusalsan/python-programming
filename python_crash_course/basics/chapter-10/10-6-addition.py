number = input("say me a number\n")
number_2 = input("say me another number and I will add to the previous number\n")
try:
    suma = int(number) + int(number_2)
except ValueError:
    print("Sorry you have to write two numbers")
else:
    print(suma)