sandwich_orders = ["mix", "double", "pastrami", "pastrami", "cheese and york ham", "pastrami"]
print("The restaurant has not got the sandwich pastrami now")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)