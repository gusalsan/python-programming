favorite_places = {"ceci": "bristol, salmanca, cabo verde", 
                   "gus": "roma, chernobyl, mexico", 
                   "migui": "california, london, hawaii"
                   }
for person, place in favorite_places.items():
    print(f"\n{person.title()}")
    print(f"{place.title()}\n")