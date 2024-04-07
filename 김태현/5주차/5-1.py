scores = [] 
for i in range(5): #5명의 점수를 입력받습니다. 
    score = int(input())

    if(score<0 or score>100 or (score%5)!=0): #점수가 0점 미만 100점 초과거나 5의 배수가 아니면 입력받지 않습니다. 
        print("잘못된 입력입니다.")
        break

    if(score<50): #50점 미만인 학생들은 50점으로 고정시킵니다. 
        score=50
    
    scores.append(score)

average = sum(scores) //5
print(average)  
