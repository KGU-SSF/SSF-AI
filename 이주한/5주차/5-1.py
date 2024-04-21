ssf = ["준서", "이다", "홍다", "우진", "우현"]
sum = 0
score = 0
avg = 0


#성능 입력
for i in range(len(ssf)):
    score = int(input(f"{ssf[i]}의 성능을 입력하세요."))

  
#조건  
    if(score<0 or score>100) :
        print("성능은 0점이상, 100점 이하여야 합니다.")
        break
    if(score%5 != 0):
        print("성능을 5의 배수로 입력해야합니다.")
        break    
    if(score<50) :
        score = 50
        sum += score

 #정상입력시       
    else:
      sum += score

#결과 계산
avg = int(sum/5)


print(avg)
