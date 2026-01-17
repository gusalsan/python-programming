responses = {}
question_active= True

while question_active:
    name  = input("What is your name?\n")
    response = input("If you can choose one place for your vacation time, where do you go?\n")

    responses[name] = response

    repeat = input("Do you want that other person response the question?\n")
    if repeat == "no":
        question_active = False
    
for name, response in responses.items():
    print(f"The perferct vacation to {name.title()} is going to:\n {response.upper()}")
