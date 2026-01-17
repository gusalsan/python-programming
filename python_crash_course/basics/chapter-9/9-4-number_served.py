class Restaurant:
    """Un ejercicio simple sobre un restaurante"""

    def __init__(self, name, cuisine_type):
        """Definimos nombre y tipo de comida para el restaurante"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        "Indicamos como se llama el restaurante y el tipo de comida que pueden degustar"
        print(f"The name of the restaurante is {self.name.upper()}")
        print(f"The type of food that you can enjoy is {self.cuisine_type}")
    
    def open_restaurant(self):
        """Indicamos que el restaurante está abierto"""
        print(f"The {self.name.upper()} is open!")
    
    def people_served(self):
        """Indicamos el número de personas atendidas"""
        print(f"The number of people served is {self.number_served}")

    def set_number_served(self, people):
        """Colocamos un valor de lectura para poder cambiar el número de mesas servidas"""
        self.number_served = people
    
    def increment_number_served(self, more_people):
        """Sumamos comensales al valor anterior"""
        self.number_served += more_people

restaurant = Restaurant("montana", "pizza")
restaurant.people_served()
restaurant.people_served()
restaurant.number_served = 23
restaurant.people_served()
restaurant.set_number_served(100)
restaurant.people_served()
restaurant.increment_number_served(50)
restaurant.people_served()
