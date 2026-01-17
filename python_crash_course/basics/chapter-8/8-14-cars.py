def car(brand, model, color, **information):
    """Hacemos un diccionario"""
    information["brand:"] = brand
    information["model:"] = model
    information ["color:"] = color
    return information

car_info = car("volkswagen", "golf", "red", year= "2004", cv="140")
print(car_info)