a = int(input())
li = []
for i in range(a):
    li.append(int(input()))

li = list(set(li))

for k in li:
    print(k)