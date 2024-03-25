a = []                 
for i in range(1,100):
    if i % 2 == 0 :        # 방법1
        a.append(i)

a = tuple(a)
print(a)


b = []
for i in range(2,100,2):
    b.append(i)            # 방법2

b = tuple(b)
print(b)