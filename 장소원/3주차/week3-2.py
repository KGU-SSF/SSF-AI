c=int(input("시험점수를 입력하세요:"))
if 90<=c<=100:
    print("A")    
else:
    if 80<=c<90:
        print("B")
    else:
        if 70<=c<80:
            print("C")
        else:
            if 60<=c<70:
                print("D")
            else:
                if 0<=c<60:
                    print("F")
                else:
                    print("다시 입력해주세요")