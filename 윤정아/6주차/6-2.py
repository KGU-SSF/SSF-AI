arr=[]
sum=0
K=int(input())
for i in range(K):
    card=int(input())
    if card!=0:
        arr.append(card)
    else:
        arr.pop()
for i in range(len(arr)):
    sum+=arr[i]
print(sum)
