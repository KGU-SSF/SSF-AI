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
        

      


