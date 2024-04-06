score=int(input("점수를 입력하시오 : "))
if(score>100 or score<0) :
    print("다시 입력하시오")
elif(score>=90) :
    print("score : A")
elif(score>=80) :
    print("score : B")
elif(score>=70) :
    print("score : C")
elif(score>=60) :
    print("score : D")
elif(score>=0) :
    print("score : F")