class ElectricCar:
    def __init__(self, make, model, year, battery):
        """Representamos los aspectos básicos de un coche"""
        self.make=make
        self.model=model
        self.year=year
        self.battery=battery
    
    def describe_car(self):
        """A little description of the car"""
        print(f"{self.make} {self.model} {self.year} {self.battery}")
    
    def upgrade_battery(self):
        """Checking the battery size and its capacity"""
        if self.battery == 40:
            range = 150
        elif self.battery == 60:
            range = 200
        
        print(f"This car can go {range} miles")

toyota = ElectricCar("toyota", "yaris", "2020", 40)
toyota.describe_car()
toyota.upgrade_battery()

toyota = ElectricCar("toyota", "yaris", "2020", 60)
toyota.describe_car()
toyota.upgrade_battery()