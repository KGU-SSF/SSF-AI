a_1, a_2, a_3, a_4 = input().split()
b_1, b_2, b_3, b_4 = input().split()
c_1, c_2, c_3, c_4 = input().split()

a_1 = int(a_1)
a_2 = int(a_2)
a_3 = int(a_3)
a_4 = int(a_4)

b_1 = int(b_1)
b_2 = int(b_2)
b_3 = int(b_3)
b_4 = int(b_4)

c_1 = int(c_1)
c_2 = int(c_2)
c_3 = int(c_3)
c_4 = int(c_4)

def First():
    if a_1 + a_2 + a_3 + a_4 == 1:
        print("C")
    elif a_1 + a_2 + a_3 + a_4 == 2: 
        print("B")
    elif a_1 + a_2 + a_3 + a_4 == 3:
        print("A")
    elif a_1 + a_2 + a_3 + a_4 == 4: 
        print("E")
    elif a_1 + a_2 + a_3 + a_4 == 0:
        print("D")
    else:
        print("다시 입력하시오")

def Second():
    if b_1 + b_2 + b_3 + b_4 == 1:
        print("C")
    elif b_1 + b_2 + b_3 + b_4 == 2:
        print("B")
    elif b_1 + b_2 + b_3 + b_4 == 3:
        print("A")
    elif b_1 + b_2 + b_3 + b_4 == 4:
        print("E")
    elif b_1 + b_2 + b_3 + b_4 == 0:
        print("D")
    else:
        print("다시 입력하시오")

def Third():
    if c_1 + c_2 + c_3 + c_4 == 1:
        print("C")
    elif c_1 + c_2 + c_3 + c_4 == 2:
        print("B")
    elif c_1 + c_2 + c_3 + c_4 == 3:
        print("A")
    elif c_1 + c_2 + c_3 + c_4 == 4:
        print("E")
    elif c_1 + c_2 + c_3 + c_4 == 0:
        print("D")
    else:
        print("다시 입력하시오")

First()
Second()
Third()