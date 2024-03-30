#1번
num = int(input())

for i in range(1,num+1):
    for j in range(num-i):
        print("0",end="")
    for k in range(i):
        print("*",end='')
    print()
