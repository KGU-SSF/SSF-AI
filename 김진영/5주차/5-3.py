for e in range(3):
    sum = 0
    s = input().split()
    for _ in s:
        sum += int(_)
    if(sum==3):
        print("A")
    elif(sum==2):
        print("B")
    elif(sum==1):
        print("C")
    elif(sum==0):
        print("D")
    else:
        print("E")