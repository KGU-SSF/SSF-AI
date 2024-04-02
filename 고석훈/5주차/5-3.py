r = [input().split() for _ in range(3)]

for i in r:
    back = i.count('1')  
    front = i.count('0')  

    if back == 0:
        print("D")  
    elif back == 1:
        print("C")  
    elif back == 2:
        print("B")  
    elif back == 3:
        print("A")  
    else:
        print("E")  