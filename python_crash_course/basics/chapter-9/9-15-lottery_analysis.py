from random import choice
from time import time

lista_random = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "w", "p", "z", "q")
counter = 0
my_ticket = [1, "w", 7, "p"]
first = choice(lista_random)
second = choice(lista_random)
third = choice(lista_random)
fourth = choice(lista_random)
ticket_winner = []
ticket_winner.append(first)
ticket_winner.append(second)
ticket_winner.append(third)
ticket_winner.append(fourth)
print(ticket_winner)
start = time()

while True:
    counter +=1
    if ticket_winner == my_ticket:
        print("CONGRATULATIONS")
        break
    else:
        first = choice(lista_random)
        second = choice(lista_random)
        third = choice(lista_random)
        fourth = choice(lista_random)
        ticket_winner = []
        ticket_winner.append(first)
        ticket_winner.append(second)
        ticket_winner.append(third)
        ticket_winner.append(fourth)
        print(ticket_winner)

print(counter)
finish = time()
print(finish-start)