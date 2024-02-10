n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
# print(scores)
# print(student_marks)

marks = student_marks[query_name]
# print(marks)
sum = 0
for i in marks:
    sum = sum + i
avr_res = sum / len(marks)
print(f'{avr_res:.2f}')
