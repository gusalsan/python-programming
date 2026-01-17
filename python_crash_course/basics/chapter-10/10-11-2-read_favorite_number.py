from pathlib import Path
import json

path = Path("number.json")
read_contents = path.read_text()
number = json.loads(read_contents)
print(f"Your favorite number is {number}")