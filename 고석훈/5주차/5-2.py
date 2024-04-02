N = int(input("높이:"))
for i in range(1, N+1):
    print(" " * (N - i), end = "")

    for p in range(i):
        print("* ", end = "")
    print("")
