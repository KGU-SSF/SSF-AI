yut_num = []

for _ in range(3) : 
    yut = list(map(int, input().split()))

    if (len(yut) != 4) :                            #윷이 범위를 벗어났을 때
        exit(0)
    if(any(num > 1 or num < 0 for num in yut)) :
        exit(0)
        
    yut_num.append(yut)
    
print("")                                           #여백
    
for yut in yut_num :
    sum = 0                                         #sum 초기화
    
    for x in yut :                                  #리스트 속 요소를 모두 더함
        sum += x
        
    if(sum == 3) :
        print("A")
    elif(sum == 2) :
        print("B")
    elif(sum == 1) :
        print("C")
    elif(sum == 0) :
        print("D")
    elif(sum == 4) :
        print("E")