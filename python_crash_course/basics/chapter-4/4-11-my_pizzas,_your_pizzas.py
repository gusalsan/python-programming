pizzas = ["margarita", "4 quesos", "barbacoa"]
friend_pizzas = pizzas[:]
pizzas.append("jamon y queso")
friend_pizzas.append("piña")
print("I don't like this pizzas:")
for pizza in pizzas:
    print(pizza.title())
print("My friends like this pizzas:")
for pizzas in friend_pizzas:
    print(pizzas.title())