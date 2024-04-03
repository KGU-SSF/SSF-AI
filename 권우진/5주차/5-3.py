yut = {}
cnt = 0

for i in range(3):
    yut[i] = input().split()
        
for i in range(len(yut)):
    for res in yut[i]:
        if res == "0":
            cnt += 1
    if cnt == 0:
        print("E")
    elif cnt == 1:
        print("A")
    elif cnt == 2:
        print("B")
    elif cnt == 3:
        print("C")
    else:
        print("D")
    cnt = 0

