#3번문제
for i in range(3):
    a = list(map(int,input().split()))
    zero = a.count(0)

    if zero == 1:
        print("A")
    elif zero == 2:
        print("B")
    elif zero == 3:
        print("C")
    elif zero == 4:
        print("D")
    else : 
        print("E")