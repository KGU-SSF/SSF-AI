a = int(input())
li = []

for i in range(a):
    b = int(input())
    if (b == 0):
        del li[len(li)-1]
    else:
        li.append(b)

print(sum(li))