a= int(input(""))
for i in range(1, a +1):
    for n in range(a-i):
        print(' ',end='')
    for n in range(i):
        print('* ', end='')
    print()