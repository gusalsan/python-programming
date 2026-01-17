prompt = "\nWelcome to the theater of Cecilandia, nice to meet you"
prompt += "\nPlease enter your age\n"
message = input(prompt)
if int(message) <= 3:
    print("Free ticket for you")
elif int(message) <= 12:
    print("10€ please")
else:
    print("15€ please")