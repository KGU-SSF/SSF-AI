arr=[]
N=int(input())
for _ in range(N):
    x=int(input())
    arr.append(x)
arr.sort()
for i in range(N):
    print(arr[i])
