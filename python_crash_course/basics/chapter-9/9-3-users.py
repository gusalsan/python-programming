class User:
    """Creamos una clase que defina un usuario de una web con su información y le mandamos un saludo"""
    def __init__(self, first_name, last_name, country, city, age):
        """Información básica del usuario"""
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.city = city
        self.age = age

    def describe_user(self):
        """Imprimimos con dos frases la info básica del usuario"""
        print(f"The name of the user is {self.first_name.title()} {self.last_name.title()} and is {self.age} years old")
        print(f"{self.first_name.title()} lives in {self.city.title()}, {self.country.title()}")

    def greet_user(self):
        """Saludamos al usuario"""
        print(f"Hi {self.first_name.title()} {self.last_name.title()}! Nice to meet you!")

bruno = User("Bruno", "Platero", "Spain", "Ourense", 30)
madri = User("Javier", "Madriñan", "Spain", "Ourense", 29)
pibe = User("Manuel", "Estanislao", "Argentina", "San Diego", 30)
bruno.describe_user()
bruno.greet_user()
madri.describe_user()
madri.greet_user()
pibe.describe_user()
pibe.greet_user()    