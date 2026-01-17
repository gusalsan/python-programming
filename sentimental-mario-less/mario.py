# Define block and ask for height
block = "#"
space = " "

# Height must be an int between 1 and 8 inclusives
while True:
    try:
        height = int(input("Height: "))
        break
    except ValueError:
        print("The height must be a number")
        height = int(input("Height: "))
while height <= 0 or height > 8:
    height = int(input("Height: "))

# Print the pyramid
for row in range(1, height+1):
    # print(f"Indice de espacio: {height-row}")
    # print(f"Indice de bloque: {row}")
    pyramid = ""
    pyramid += (space*(height-row))
    pyramid += (block*row)
    print(pyramid)
