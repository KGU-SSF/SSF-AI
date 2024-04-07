score = int(input("시험 점수를 입력하십시오"))

while 1 : 
    if score > 100 :
        print("다시 입력해주세요")
        continue
    elif score >= 90 :
        print("A")
        break
    elif score >= 80 :
        print("B")
        break
    elif score >= 70 :
        print("C")
        break
    elif score >= 60 :
        print("D")
        break
    elif score < 60 :
        print("F")
        break
    elif score <= 0 :
        print("다시 입력해주세요")
        continue
        
            