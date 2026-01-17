friend_1 = {"name": "alex", "last name": "lopez", "age": 28, "city": "el Puente"}
friend_2 = {"name": "miguel", "last name": "blanco", "age": 29, "city": "Lagunas"}
friend_3 = {"name": "congui", "last name": "negro", "age": 28, "city": "GardaCan"}
people = [friend_1, friend_2, friend_3]
for friend in people:
    full_name = f"{friend["name"]} {friend["last name"]}"
    information = f"{friend["age"]}\n{friend["city"]}\n"
    print(f"{full_name.title()}: \n {information.title()}")