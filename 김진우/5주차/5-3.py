for i in range(3):
    a = list(map(int, input().split()))
    if a.count(0) == 1:
        print("A") #도
    elif a.count(0) == 2:
        print("B") #개
    elif a.count(0) == 3:
        print("C") #걸
    elif a.count(0) == 4:
        print("D") #윷
    else:
        print("E") #모