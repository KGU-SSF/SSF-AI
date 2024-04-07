x=int(input("숫자를 입력하시오:"))
for i in range(1,x+1):
    for j in range(x-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print(' ')