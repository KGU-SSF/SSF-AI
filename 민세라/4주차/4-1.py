n = int(input())
t = n-1

for i in range(n):
    print(' '*t+'*'*(i+1))
    t-=1