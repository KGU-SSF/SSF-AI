score=int(input("점수를 입력하세요 : "))

if score>100 or score<0:
    print("다시 입력해주세요")
elif(score>=90):
    print("A")
elif(score>=80):
    print("B")
elif(score>=70):
    print("C")
elif(score>=60):
    print("D")
else:
    print("F")