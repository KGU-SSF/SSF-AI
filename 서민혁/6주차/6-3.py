a=int(input())
b=[]
for i in range(a):
    b.append(input())
b.sort()
for i in range(a):
    print(b[i])