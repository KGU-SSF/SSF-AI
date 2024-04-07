l = int(input('숫자를 입력하세요: '))

if l < 0 or l > 100:
    print('Error')
    exit()

for i in range(1, l+1):
    print(' ' * (l - i), end = '')

    for j in range(i):
        print('* ', end = '')

    print()
        
   

    
