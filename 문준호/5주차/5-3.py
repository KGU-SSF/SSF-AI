list1 = list()
for i in range(3):
    list1.append(list(map(int, input().split(" "))))

for i in list1:
    sum = 0
    for j in i:
        sum += j
    if sum == 3:
        print("A")
    elif sum == 2:
        print("B")
    elif sum == 1:
        print("C")
    elif sum == 4:
        print("D")
    elif sum == 0:
        print("E")