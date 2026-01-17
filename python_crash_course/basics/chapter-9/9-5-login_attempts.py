class User:
    """Creamos una clase que defina un usuario de una web con su información y le mandamos un saludo"""
    def __init__(self, first_name, last_name, country, city, age):
        """Información básica del usuario"""
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.city = city
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Imprimimos con dos frases la info básica del usuario"""
        print(f"The name of the user is {self.first_name.title()} {self.last_name.title()} and is {self.age} years old")
        print(f"{self.first_name.title()} lives in {self.city.title()}, {self.country.title()}")

    def greet_user(self):
        """Saludamos al usuario"""
        print(f"Hi {self.first_name.title()} {self.last_name.title()}! Nice to meet you!")
    
    def increment_login_attempts(self):
        """Sumamos uno cada vez que llamemos a este método e imprimimos el valor"""
        self.login_attempts+=1
        print(f"Number of login attemts is: {self.login_attempts}")

    def reset_login_attempts(self):
        """Reseteamos el valor de login attempts a 0"""
        self.login_attempts = 0
        print(f"Your number of login attempts is {self.login_attempts}")

bruno = User("Bruno", "Platero", "Spain", "Ourense", 30)
bruno.increment_login_attempts()
bruno.increment_login_attempts()
bruno.increment_login_attempts()
bruno.increment_login_attempts()
bruno.increment_login_attempts()
bruno.reset_login_attempts()
bruno.increment_login_attempts()