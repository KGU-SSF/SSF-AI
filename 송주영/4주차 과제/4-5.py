#5번
list = []
for i in range(1, 100):
    if i%2 ==0:
        list.append(i)
list_tuple = tuple(list)
print(list_tuple)