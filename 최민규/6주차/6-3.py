n = int(input())
arr=[]
for _ in range(n):
    k = int(input())
    arr.append(k)
arr.sort()
for i in arr:
    print(i)