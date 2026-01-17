def make_pizza(size, *toppings):
    """función que hace pizza"""
    print(f"Haciendo pizza con tamaño {size} y los siguientes toppings:")
    for topping in toppings:
        print(topping.title())