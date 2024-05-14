h = int(input())
i = 0
j = 0
for i in range(h):
    print(" "*(h-i), end="") 
    for j in range(i):
        print("*", end=" ")
    print("*")