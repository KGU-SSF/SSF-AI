n = int(input())
n = n + 1

for x in range(0, n) :
    print(str("*" * x).rjust(n-1))