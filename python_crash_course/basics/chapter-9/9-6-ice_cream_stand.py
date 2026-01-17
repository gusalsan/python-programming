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

class IceCreamStand(Restaurant):
    """Un subtipo de restaurante"""
    def __init__(self, name, cuisine_type, flavours):
        """Atributos iniciales del restaurante y añadimos flavours"""
        super().__init__(name, cuisine_type)
        self.flavours = flavours
    def flavours_list(self):
        """Una lista de los sabores de los helados"""
        print(f"We have this flavours avaliable:\n{self.flavours}")

ibense = IceCreamStand("ibense", "ice-creams", "orange, apple, strawberry, chocolate and nuts")
print(ibense.describe_restaurant())
print(ibense.flavours_list())