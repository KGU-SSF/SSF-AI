a = []
for i in range(3):
    a.append(input().split())
for i in range(3):
    if a[i].count('1') == 0:
        print("D")
    elif a[i].count('1') == 1:
        print("C")
    elif a[i].count('1') == 2:
        print("B")
    elif a[i].count('1') == 3:
        print("A")
    elif a[i].count('1') == 4:
        print("E")