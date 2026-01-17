from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()
for line in contents.splitlines():
    line = contents.replace("Python", "C")
print(line)