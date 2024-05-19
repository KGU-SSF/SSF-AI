n = int(input())
if n<0 or n>100 :
    n = int(input("1<=n<=100:"))
for i in range(n):
    print("{0}{1}".format(' '*(n-i-1),' '.join('*'*(i+1))))