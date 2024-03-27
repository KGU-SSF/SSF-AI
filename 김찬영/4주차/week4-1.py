n = int(input("별 개수를 입력해주세요:"))
for i in range(1, n+1, +1):
    for j in range(i, n, +1):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
