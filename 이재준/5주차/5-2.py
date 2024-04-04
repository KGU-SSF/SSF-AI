n = int(input())
n= n + 1

for x in range(1, n) :
    print(" " * (n - x), end = "")  
    for _ in range(x):
        print("* ", end="")         
    print("") 
