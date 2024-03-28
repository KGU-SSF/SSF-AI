a = int(input("별 갯수 입력:"))

b=1 
while b <= a:
    print(' '*(a-b)+'*'*b)
    b += 1