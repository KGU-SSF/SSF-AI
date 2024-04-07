a=int(input())
for i in range(1,a+1):
    for j in range(0,a-i):
        print(" ",end="")
    for k in range(0,i):
        print("* ",end="")
    print("")