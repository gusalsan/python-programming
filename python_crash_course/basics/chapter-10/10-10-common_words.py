from pathlib import Path

path = Path("gutenberg.txt")
contents = path.read_text(encoding="utf-8")
words = contents.splitlines()
#number_words = len(words)
#print(number_words)

for line in words:
    line = "and the ransomed people—Angels and Saints together—sing the Lord’s"
    count_and = line.count("and")
    print(count_and)

number_of_the = contents.lower().count("the ")
print(number_of_the)