
    n = int(input("점수: "))

    if n >= 90 and a<=100:
        print("A")
    elif n >= 80:
        print("B")
    elif n >= 70:
        print("C")
    elif n >= 60:
        print("D")
    elif n < 60 and a>=0:
        print("F")
    else:
        print("다시 입력해주세요")
