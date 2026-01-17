from random import choice
import time

lottery_numbers = ["a", "b", "c", "d", "1", "2", "3", "4", "5"]
my_ticket = ["1", "d", "a", "1"]
counter = 0
start = time.time()

while True:
    counter = counter+1
    ticket_winner = []
    for n in range(len(my_ticket)):
        item = choice(lottery_numbers)
        ticket_winner.append(item)
    print(ticket_winner)
    
    if my_ticket == ticket_winner:
        break

finish = time.time()
print(counter)
duration = finish - start
print(duration)