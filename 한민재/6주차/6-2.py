a = int(input())
list = []
for i  in range(a):
    c = int(input())
    if c == 0:
        list.pop()
    else:
        list.append(c)
print(sum(list))

        

