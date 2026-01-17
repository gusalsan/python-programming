from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()
print(contents)

lines = contents.splitlines()
one_line = ""
for line in lines:
    one_line += line
    print(one_line)