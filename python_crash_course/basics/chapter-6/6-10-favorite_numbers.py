favourite_numbers = {"bruno": "10 and 5", 
                     "miguel": "13 and 5", 
                     "madriñan": "7 and 1", 
                     "angel": "9 and 2", 
                     "cachi": "14 and 4"
                     }
for name, number in favourite_numbers.items():
    print(f"The favorite numbers of {name.title()} are:")
    print(number)