student = []
sum = 0
for i in range(5):
    score = int(input("%d번째 학생의 점수를 입력하시오 : "%(i+1)))
    if score > 50:
        student.append(score)
    else:
        student.append(50)

for i in student:
    sum += i

avg = sum/5
print("평균 : %0.2f" %avg)
