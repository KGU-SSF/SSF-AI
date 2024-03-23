a = int(input("시험 점수를 입력 하시오  : "))

if(a>100 or a<0):
    print("다시 입력 해주세요.")
elif(a>=90):
    print("A")
elif(a>=80):
    print("B")
elif(a>=70):
    print("C")
elif(a>=60):
    print("D")
else:
    print("F")