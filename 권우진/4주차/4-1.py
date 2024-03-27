# 1번
num = int(input("입력: "))

for i in range(num):
    for j in range(num - i - 1):
        print("-", end="")
    
    for k in range(i + 1):
        print("*", end="")
    print()
