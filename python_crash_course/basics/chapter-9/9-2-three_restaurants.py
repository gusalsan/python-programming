class Restaurant:
    """Un ejercicio simple sobre un restaurante"""

    def __init__(self, name, cuisine_type):
        """Definimos nombre y tipo de comida para el restaurante"""
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        "Indicamos como se llama el restaurante y el tipo de comida que pueden degustar"
        print(f"The name of the restaurante is {self.name.upper()}")
        print(f"The type of food that you can enjoy is {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"The {self.name.upper()} is open!")

josu_restaurant = Restaurant("Valilongo", "traditional galician food")
baños_de_molgas_restaurant = Restaurant("Foxo", "Meat")
carballiño_restaurant = Restaurant("Fuchela", "octopus")
josu_restaurant.describe_restaurant()
baños_de_molgas_restaurant.describe_restaurant()
carballiño_restaurant.describe_restaurant()