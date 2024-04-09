total = 0
students = []

for i in range(5):
    score = int(input())
    if (score < 50) :
        score = 50
    students.append(score)
    total += score

average = total / 5
print(int(average))