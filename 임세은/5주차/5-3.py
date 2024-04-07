arr = [[0] * 4 for _ in range(3)]

for i in range(3):
    arr[i]=list(map(int,input().split()))

result=[0]*3

for i in range(3):
    for k in range(4):
        result[i]+=arr[i][k]

for i in range(3):
    if result[i]==0:
        print("D")

    elif result[i]==1:
        print("C")

    elif result[i]==2:
        print("B")

    elif result[i]==3:
        print("A")

    elif result[i]==4:
        print("E")