ls = []

for i in range(1,100):
    if i % 2 == 0:
        ls.append(i)

ls = tuple(ls)
print(ls)