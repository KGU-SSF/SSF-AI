a = b = n = int(input())
a = a - 1
b = b - n + 1
for i in range(1, n+1):
    print(" "*a,"*"*b)
    a = a - 1
    b = b + 1