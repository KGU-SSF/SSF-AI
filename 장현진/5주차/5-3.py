for e in range(3): #3번 반복하기
    sum = 0#변수 지정하기
    s = input().split() #사용자에게 입력받은것을 공백을 기준으로 나누어서 리스트에 넣기
    for _ in s:
        sum += int(_) #문자형인 요소들을 int(_)의 _자리에 넣어 정수형으로 바꿔준후 sum에다 더하기
    if(sum==3):
        print("A")
    elif(sum==2):
        print("B")
    elif(sum==1):
        print("C")
    elif(sum==0):
        print("D")
    else:
        print("E")#sum을 기준으로 조건문에 맞게 print하기