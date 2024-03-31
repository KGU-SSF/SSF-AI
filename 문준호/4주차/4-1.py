N = int(input("input N : "))

for i in range(1, N+1):
    for j in range(N+1 - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print("")

       