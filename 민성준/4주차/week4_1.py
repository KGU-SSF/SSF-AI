n = int(input("최대 별의 개수를 입력하시오 : "))

for i in range(1,n+1):
    k = n - i
    for p in range(0,k):
        print(" ",end = "")
    for l in range(0,i):
        print("*",end = "")
    
    print("\n")