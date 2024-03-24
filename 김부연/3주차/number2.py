score = int(input("시험 점수를 입력하세요: "))

while 1:
    if 90 <=score <=100:
        print("A")
        break
    elif 80<=score <=89:
        print("B")
        break
    elif 70<=score <=79:
        print("C")
        break
    elif 60<=score <=69:
        print("D")
        break
    elif score >100:
        score = int(input("다시입력해주세요:"))
    elif score<0:
        score = int(input("다시입력해주세요:"))
    else:
         print("F")
         break
