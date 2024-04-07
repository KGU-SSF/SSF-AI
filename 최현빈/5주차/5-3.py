for i in range(3):
    a = list(map(int, input().split()))
    if a.count(0) == 1:
        print("A")
    if a.count(0) == 2:
        print("B")
    if a.count(0) == 3:
        print("C")
    if a.count(0) == 4:
        print("D")
    if a.count(1) == 4:
        print("E")