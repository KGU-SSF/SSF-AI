print("시험점수를 입력하세요")
a = int(input())

if(a>100):
    print("다시 입력해주세요")

elif(a>=90 and a<=100100):
    print("A")

elif(a>=80 and a<90):
    print("B")

elif(a>=70 and a<80):
    print("C")

elif(a>=60 and a<70):
    print("D")

else:
    print("F")