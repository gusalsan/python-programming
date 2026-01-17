message = input("Tell me a number and I will say you if is a multiple of ten: ")
if int(message) % 10 == 0:
    print("Yes, it is")
else:
    print("No, it isn't")