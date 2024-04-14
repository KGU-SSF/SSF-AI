sum = 0                                                 #변수 초기화

for i in range(5):                                      #5번 반복
    score = int(input())                                #점수 입력
    
    if score < 0 or score > 100 or score % 5 != 0:      #점수를 조건과 다르게 잘못 입력한 경우 프로그램 종료
        print("점수를 올바르게 입력해주세요")
        exit(0)
    
    elif score < 50:                                    #점수가 50점 이하인 경우 50점으로 설정
        score = 50
    
    sum += score                                        #입력 받은 점수를 총합에 더함

average = (sum//5)                                      #평균 계산
print(average)                                          #평균 출력