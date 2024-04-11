a=int(input("줄의 개수: "))
b=[]
for i in range(a):
    b.append(int(input()))
    if b[-1]==0:
        b.remove(b[-1])
        for i in range(b.count(b[-1])):
            b.remove(b[-1])
    elif b[-1]>9 or b[-1]<0:
        b.remove(b[-1])
print("총합 :", sum(b))                