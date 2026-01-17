students = ["gus", "bruno", "toni"]
scores = [0, 5, 8]
gus_score = scores[0]

students_scores = {"gus": 0, "bruno": 0, "toni": 8}

print(students)
print(scores)
print(gus_score)
print(students_scores)
print(students_scores)
print(students_scores["gus"])
print(students_scores["gus"])
print(students_scores)

for score in set(students_scores.values()):
    print(score)