N = int(input())                    #높이 N입력

for i in range(1, N+1):             #높이만큼 반복
    print(" " * (N - i), end = "")  #공백 넣기 

    for s in range(i):              
        print("* ", end = "")       #갯수만큼 반복해서 *이랑 공백넣기
        
    print("")                       #다음줄