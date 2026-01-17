prompt = "\nHola Ceci, bienvenida a esta prueba de fuego"
prompt += "\nTendrás que superar 3 desafíos para ganar esta prueba"
prompt += "\nTus respuetas tendrán que estar en minúscula y sin acentos"
prompt += "\nPrimera pregunta:"
prompt += "\n¿Vamos a follar hoy?\n"
message = ""
while message != "si":
    message = input (prompt)
    if message != "si":
        print(f"Tu respuesta {message.upper()} es incorrecta, inténtalo de nuevo")

prompt = "\nAndas caliente ultimamente, a ver si nos vamos relajando"
prompt += "\nBueno vamos con la siguiente prueba"
prompt += "\n¿Cuántas veces me preguntaste ayer si quería el saco de granos de los cojones? (escribe un número)\n"
active=True
while active:
    message = input(prompt)
    if int(message) == 10:
        active = False
    else:
        print("No es correcto tronca, inténtalo de nuevo")

prompt = "\nNunca pensé que llegarías tan lejos, estoy tan orgulloso..."
prompt += "\nÚltima prueba:"
prompt += "\nSoy alto cuando soy joven, y corto cuando soy viejo. ¿Qué soy? Ánimo princesa\n"
while True:
    message = input(prompt)
    if message == "vela":
        print("Enhorabuena princesa, has superado el reto, te mereces un chiriflú")
        break
    else:
        print("Errooooooooooor, piensa un poco más y no desesperes")