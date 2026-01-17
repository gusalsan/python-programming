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

restaurant = Restaurant("Montana", "pizza")
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()