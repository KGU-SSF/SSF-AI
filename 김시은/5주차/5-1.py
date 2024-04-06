sum = 0
for i in range(5):
    score = int(input())
    if score<50:
        score = 50
    sum += score
    
sum = sum / 5

print("평균 성능 : " + str(sum))





