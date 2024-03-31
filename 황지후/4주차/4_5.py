list = []

for i in range(1, 99 + 1):
    if i % 2 == 0:
        list.append(i)

tup = tuple(list)
print (tup)