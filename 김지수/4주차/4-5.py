even = []

for i in range (1, 100) :
    if i % 2 == 0 :
        even.append(i)
    else :
        continue
    
print(tuple(even))