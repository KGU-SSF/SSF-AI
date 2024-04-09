sum = 0

for i in range(5):
    score = int(input())
    if(score < 50): score = 50
    sum += score

print(int(sum/5))