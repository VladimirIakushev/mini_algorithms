list_students = []
scores = []
list_names = []
for n in range(int(input())):
    name = input()
    score = float(input())
    res = [name, score]
    list_students.append(res)
for student in list_students:
    scores.append(student[1])
sorted_scores = set(scores)
sorted_scores = sorted(list(sorted_scores))
print(sorted_scores)
second_grade = sorted_scores[1]
for student in list_students:
    if student[1] == second_grade:
        list_names.append(student[0])
list_names.sort()
for name in list_names:
    print(name)
