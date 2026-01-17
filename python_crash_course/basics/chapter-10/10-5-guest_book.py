#EN ESTE EJERCICIO SOLO ME AÑADE A GUEST EL ULTIMO NOMBRE DADO
from pathlib import Path

path = Path("guest.txt")
prompt = "Tell me your name"
prompt += "\nIf you want to exit, write 'stop'\n"
list_names = []


while True:
    names = input(prompt)
    if names == "stop":
        break
    list_names.append(names)

for name in list_names:
    guest_info += f"{name}\n"
path.write_text(guest_info)
    