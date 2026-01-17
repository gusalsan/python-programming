pet_1 = {"animal": "dog", "size": "medium"}
pet_2 = {"animal": "bird", "size": "very small"}
pet_3 = {"animal": "cat", "size": "small"}
pets = [pet_1, pet_2, pet_3]
for pet in pets:
    type_of_animal = (f"{pet["animal"]}")
    size_of_animal = (f"{pet["size"]}")
    print(f"My favourite animal is a {type_of_animal} I like it because is {size_of_animal}")