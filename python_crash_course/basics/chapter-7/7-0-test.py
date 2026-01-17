#age = input("tell me your age: ")
#print(f"your age is {age}")

#prompt = "I would like to know your name\n"
#prompt += "Tell me your name, please: "
#name = input(prompt)
#print(f"hello {name}")

#numero = "2"
#numero_entero = int(numero)
#print(numero)
#print(numero_entero)

#altura = input("¿Cuánto mides?: ")
#altura = int(altura)
#if altura > 30:
 #   print("puedes subir")
#elif altura < 30:
 #   print("no puedes subir")

#current_number = 1
#while current_number <= 200000:
#    print(current_number)
#    current_number += 1

prompt = "\nDime algo y lo repito"
prompt += "\nSi quieres que pare di: para\n"
active = True
while active:
    message = input(prompt)
    if message == "para":
        active = False
    if message == "para ya":
        active = False
    else:
        print(message)