#2번문제
N = int(input("숫자"))

for i in range(1,N+1):
    for j in range(1,N-i+1):
        print(' ',end ="")
    for j in range(1,i+1):
        print('* ',end ="")
    print('')