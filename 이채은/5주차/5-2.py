n = int(input("숫자를 입력하세요:"))
for i in range(1, n+1):
     for j in range(n-i):
        print(" ", end="")
     for j in range(i):
        print("*", end="")
        print(" ", end="")
     print()