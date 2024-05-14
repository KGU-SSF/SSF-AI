l=[]
n=int(input())
for i in range(n):
    a=int(input())
    if a!=0:
        l.append(a)
    else:
       l.pop()
print(sum(l))