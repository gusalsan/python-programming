def describes_city(name, country="spain"):
    """"Damos una frase con una ciudad y el pais"""
    print(f"{name.title()} is in {country.title()}")
describes_city("ourense")
describes_city("almeria")
describes_city("lugo")
describes_city("london", "United Kingdom")