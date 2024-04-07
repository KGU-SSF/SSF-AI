sum = 0

for i in range(5):
    score = int(input())
    
    if score < 0 or score > 100 or score % 5 != 0:
        print("점수를 올바르게 입력해주세요")
        exit(0)
    
    elif score < 50:
        score = 50
    
    sum += score

average = (sum//5)
print(average)