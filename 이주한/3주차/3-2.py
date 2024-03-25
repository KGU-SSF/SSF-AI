score = int(input("시험 점수를 입력하세요 : "))

if(90<=score<=100):
    print("A")
elif(80<=score<=89):
    print("B")
elif(70<=score<=79):
    print("C")
elif(60<=score<=69):
    print("D")
elif(0<=score<=59):
    print("F")
else:
    print("다시 입력해주세요")