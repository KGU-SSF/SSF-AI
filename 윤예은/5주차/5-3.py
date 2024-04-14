def play(yut1, yut2, yut3, yut4): #네 개의 윷을 던지는 함수 정의 
    count=yut1+yut2+yut3+yut4 #등(1)의 합
    
    if count==0: 
        return 'D' #윷
    elif count==1:
        return 'C' #걸
    elif count==2:
        return 'B' #개
    elif count==3:
        return 'A' #도
    elif count==4:
        return 'E' #모

Y=[] #빈 리스트 생성
for _ in range(3): #반복문을 사용해 3번의 입력을 받음
    yuts = input().split() #입력된 값들을 공백을 기준으로 나누어 리스트를 받음
    yut1, yut2, yut3, yut4 = map(int, yuts) #yuts에서 입력받은 값으로 각 값들을 정수로 변환함

    if yut1 not in [0,1] or yut2 not in [0,1] or yut3 not in [0,1] or yut4 not in [0,1]:
        print('0과 1로 입력해주세요.') #모든 윷의 값들이 0과 1이 아니면 오류 메세지를 출력하고 프로그램을 중단함
        break
    result=play(yut1,yut2,yut3,yut4) #입력된 값들이 모두 올바른 경우 play함수를 사용해 결과를 계산함
    Y.append(result) #Y리스트에 추가함

for result in Y:
    print(result) #모든 결과를 출력


    

