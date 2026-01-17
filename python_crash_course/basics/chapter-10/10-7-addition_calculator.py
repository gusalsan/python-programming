while True:
    number = input("say me a number, if you want to exit, write 'exit'\n")
    if number == "exit":
        break
    number_2 = input("say me another number and I will add to the previous number\n")
    if number_2 == "exit":
        break
    try:
        suma = int(number) + int(number_2)
    except ValueError:
        print("Sorry you have to write two numbers")
    else:
        print(suma)
    
        
   