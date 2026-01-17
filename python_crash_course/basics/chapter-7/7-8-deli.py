sandwich_orders = ["mix", "double", "cheese and york ham"]
finished_sandwiches = []

#primero le decimos al cliente/s que su sandwich está siendo realizado
for sandwich in sandwich_orders:
    print(f"We are making your {sandwich} sandwich")

#ahora movemos los sandwich de la lista de pedidos a la lista de finalizados
#si no uso el while loop solo me hace pop del último elemento de la lista
while sandwich_orders:
    move_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(move_sandwich)

#Le decimos al cliente que su pedido está listo
for sandwich in finished_sandwiches:
    print(f"You can take your {sandwich} sandwich")