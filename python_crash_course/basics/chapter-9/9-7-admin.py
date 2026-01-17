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

class Admin(User):
    """Lista de privilegios que tiene el administrador"""
    def __init__(self, first_name, last_name, country, city, age, privileges):
        """Lista inicial como usuario mas a mayores añadimos los privilegios"""
        super().__init__(first_name, last_name, country, city, age)
        privileges = ("Can delete post", "Can ban user", "Can add post")
        self.privileges = privileges

    def show_privileges(self):
        """Imprimimos la lista de privilegios del admin"""
        print(f"Admin {self.first_name} have these privileges:\n{self.privileges}")

admin = Admin("Iago", "Aspas", "Spain", "Moaña", 37, "privileges")
print(admin.describe_user())
print(admin.show_privileges())
