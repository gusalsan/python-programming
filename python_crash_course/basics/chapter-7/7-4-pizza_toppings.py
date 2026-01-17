prompt = "\n Please enter a topping to your pizza: "
prompt += "\n If you finish please write 'finish' \n"
sesion = True
while sesion:
    message = input(prompt)
    if message == "finish":
        print("Thanks for your delivery")
        sesion = False
    else:
        print(f"Adding {message.upper()}")