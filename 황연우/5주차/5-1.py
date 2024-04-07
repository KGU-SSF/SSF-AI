n=int(input())
for i in range(1, n+1): 
    for k in range(n-i):
        print(' ', end='')
    for k in range(i):
        print('* ', end='')
    print()
    
#정수를 입력받고,n에 따라 삼각형 높이 출력, 삼각형 공백 출력,*출력

    

