s = int(input())
b = s-1

for i in range(1,s+1):
    print(' '*b,end='')
    for j in range(i):
        print('* ',end='')
    b-=1
    print('')