while True:                          #줄의 개수를 1부터 100사이로 입력받기
    a=int(input("줄의 개수: "))
    if 1<=a<=100:
        break 
for i in range(a):                    #줄의 개수 만큼 반복
    print(" "*(a-i-1)+"*"+(" "+"*")*i)   # 각 줄에 해당하는 별의 개수와 공백 출력
