#magos = ["merlin", "harry potter", "alice"]
#for mago in magos:
#    print(mago)
#bruno = "bruno"
#for i in range (1, 5):
#    print(bruno)

n=int(input())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6<= n <= 20:
    print("Weird")
else:
    print("Not Weird")