import json
from pathlib import Path

question_number = input("What is your favorite number?\n")
path = Path ("number.json")
contents = json.dumps(question_number)
path.write_text(contents)