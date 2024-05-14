a = []*5
sum=0
for i in range(5):
    a.append(int(input()))
    if a[i]<50: a[i]=50
    sum=sum+a[i]

print(int(sum/5))