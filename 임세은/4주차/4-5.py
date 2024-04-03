t1=()
l1=list(t1)
for i in range(1,100):
    if i%2==0:
        l1.append(i)
    else:
        continue

t1=tuple(l1)

print(t1)

