while True:
    score=int(input("입력예시:"))
    
    if score>=90 and score<=100:
        print("A")
        break
    elif score>=80 and score<=89:
        print("B")
        break
    elif score>=70 and score<=79:
        print("C")
        break
    elif score>=60 and score<=69:
        print("D")
        break
    elif score<60 and score>=0:
        print("F")
        break
    else:
        print("다시입력해주세요")
        continue