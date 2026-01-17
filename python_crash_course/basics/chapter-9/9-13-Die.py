from random import randint
class Die_6:
    """Haremos un dado con diferente número de caras"""
    def __init__(self, sides):
        """Definimos el número de caras que tiene el dado"""
        self.sides = sides
        self.sides = 6
    
    def roll_die(self):
        """Hacemos que salga un número al azar entre 0 y el número de caras"""
        print(randint (0, self.sides))

die = Die_6("x")
print(die.roll_die())



class Die_10:
    """Haremos un dado con diferente número de caras"""
    def __init__(self, sides):
        """Definimos el número de caras que tiene el dado"""
        self.sides = sides
        self.sides = 10
    
    def roll_die(self):
        """Hacemos que salga un número al azar entre 0 y el número de caras"""
        print(randint (0, self.sides))

die = Die_10("x")
print(die.roll_die())



class Die_20:
    """Haremos un dado con diferente número de caras"""
    def __init__(self, sides):
        """Definimos el número de caras que tiene el dado"""
        self.sides = sides
        self.sides = 20
    
    def roll_die(self):
        """Hacemos que salga un número al azar entre 0 y el número de caras"""
        print(randint (0, self.sides))

die = Die_20("x")
print(die.roll_die())