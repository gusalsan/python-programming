def city_country(city, country):
    """"Return the two names nearly formatted"""
    full_message = f"{city}, {country}"
    return full_message.title()
print(city_country("ourense", "españa"))
print(city_country("new york", "estados unidos"))
print(city_country("paris", "francia"))