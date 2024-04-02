n = int(input("줄 개수 입력: "))

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print("", end =" ")
    for k in range (1, i+1):
        print("*", end =" ")
    print("\n")