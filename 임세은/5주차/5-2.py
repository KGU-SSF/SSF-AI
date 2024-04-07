n=int(input("숫자를 입력하시오:"))

for i in range(n):
    
    for k in range(n-1,i,-1):
        print(" ",end="")

    for j in range(1,i+2):
        print("* ",end="")
    print()