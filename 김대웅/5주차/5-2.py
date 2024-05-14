n = int(input("숫자를 입력하시오 :"))

for i in range(0, n+1, 1):
    for j in range(0, n-i, 1):  
        print(" ",end="")
    for k in range(0, i, 1):
        print("* ",end="")
    print("")