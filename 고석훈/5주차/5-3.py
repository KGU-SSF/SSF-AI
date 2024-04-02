r = [input().split() for _ in range(3)]

for i in r:
    back = i.count('1')  #뒷면 수
    front = i.count('0')  #앞면 수

    if back == 0:
        print("D")  #윷
    elif back == 1: 
        print("C")  #걸
    elif back == 2:
        print("B")  #개
    elif back == 3:
        print("A")  #도
    else:
        print("E")  #모
    