scores = [] 
for i in range(5):
    score = int(input())

    if(score<0 or score>100 or (score%5)!=0):
        print("잘못된 입력입니다.")
        break

    if(score<50):
        score=50
    
    scores.append(score)

average = sum(scores) //5
print(average)  
