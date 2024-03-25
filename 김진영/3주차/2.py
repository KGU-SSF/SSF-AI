gr = int (input("점수를 입력하시오 : "))
if 90<= gr <= 100 :
    print("A")
else:
    if 80 <= gr < 90 :
         print("B")
    else:
        if 70<= gr < 80 :
            print("C")
        else:
            if 60<= gr <69 :
                print("D")
            else :
                if 0<= gr <60 :
                    print("F")                 
                else :    
                    print("다시 입력")