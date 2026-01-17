from pathlib import Path

cat_path = Path("cats.txt")
dog_path = Path("dogs.txt")

try:
    cats_names = cat_path.read_text()
    dogs_names = dog_path.read_text()
    print(cats_names)
    print(dogs_names)
except FileNotFoundError:
    pass