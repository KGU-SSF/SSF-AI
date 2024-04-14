k = int(input())
arr=[]
for _ in range(k):
    i = int(input())
    if i==0:
        arr.pop()
        continue
    arr.append(i)
print(sum(arr))