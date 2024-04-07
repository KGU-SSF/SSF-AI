num = int(input("입력 : "))

for i in range(1, num+1):
    print(" "*(num - i), end="")
    for j in range(1, i+1):
        print("*", end="")
        print(" ", end="")
    print("")