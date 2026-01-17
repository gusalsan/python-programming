from pathlib import Path

name = input("Tell me you name: ")
path = Path("guest.txt")
path.write_text(name)