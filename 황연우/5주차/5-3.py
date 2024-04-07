for x in range(3):
    a, b, c, d=(map(int,input().split()))

    if a+b+c+d == 1:
        print('C')
    elif a+b+c+d == 2:
        print('B')
    elif a+b+c+d == 3:
        print('A')   
    elif a+b+c+d == 4:
        print('E')
    else:
        print('D')   
        
# for 반복문을 사용해 3번 반복하고, a,b,c,d를 입력받고 
# if를 사용해 변수를 모두 더한값이 1이 되면 걸이 출력되게 하고
# 2가 되면 개, 3이 되면 도, 4가 되면 모를 출력하고, 
#else를 사용해 윷을 출력하게 한다
      


