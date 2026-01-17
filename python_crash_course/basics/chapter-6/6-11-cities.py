cities = {
    "roma": {"country": "italy", 
             "population": 2760000, 
             "fact": "It was the most important city in history"}, 
    "ourense": {"country": "spain", 
                "population": 106000, 
                "fact": "It is not known out of Spain"}, 
    "vigo": {"country": "Spain", 
             "population": 360000, 
             "fact": "It has the most important team of football in Galicia"}
}
for city, city_info in cities.items():
    good_info = f"{city_info["country"]}\n{city_info["population"]}\n{city_info["fact"]}"
    print(f"\n{city.title()}:\n{good_info}")