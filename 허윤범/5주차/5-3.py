for i in range(3): 
    a = list(map(int, input().split())) #split으로 공백을 통해 분리하고 map을 통해 정수로 변환하여 list에 저장한다
    if a.count(0) == 1: #0의 수를 세어 출력한다
        print("A")
    elif a.count(0) == 2:
        print("B")
    elif a.count(0) == 3:
        print("C")
    elif a.count(0) == 4:
        print("D")
    else:
        print("E")