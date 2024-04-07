n = int(input())

for i in range(1, n+1):
    for j in range(0, n-i):
        print(" ", end = "")
    for k in range(0, i):
        print("* ", end = "")
        
    print("")