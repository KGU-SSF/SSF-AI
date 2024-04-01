n = int(input("인원을 입력하세요"))
scores = []
sum = 0

for i in range(0,n):
    score = int(input("점수를 입력하세요: "))
    if(score<50):
        score = 50
    scores.append(score)
    
for i in range(0,n):
    sum = sum + scores[i]

average = sum / n 

print(int(average))
