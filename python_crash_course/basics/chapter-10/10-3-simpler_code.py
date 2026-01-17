from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()

one_line = ""
for line in contents.splitlines():
    one_line += line
    print(one_line)