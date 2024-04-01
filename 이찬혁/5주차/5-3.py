yoots =[]
for a in range(0,3):
    yoots.append(input())
for a in range(0,3):
    yoot = yoots[a].split()
    result = 0
    for i in range(0,4):
    
        if yoot[i] == "0":
           result += 1

    if result == 0:
        print("D")
    if result == 1:
        print("A")
    if result == 2:
        print("B")
    if result == 3:
        print("C")
    if result == 4:
        print("E")