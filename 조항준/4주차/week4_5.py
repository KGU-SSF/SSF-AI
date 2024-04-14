even_list = []

for i in range(1,100):
    if(i % 2 == 0):
        even_list.append(i)

even = tuple(even_list)
        
print(even)