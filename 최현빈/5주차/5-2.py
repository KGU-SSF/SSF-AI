n = int(input())                 #n 입력

for i in range(1, n+1):          #출력할 층수 결정
    for j in range(0, n-i):      #공백 출력
        print(" ", end = "")
    for k in range(0, i):        #별 출력
        print("* ", end = "")
        
    print("")                    #줄바꿈