print("점수를 입력하시오:")
jumsu=int(input())

if(jumsu>=90 and jumsu<=100):
    print("A")
    
elif(jumsu>=80 and jumsu<90):
    print("B")

elif(jumsu>=70 and jumsu<80):
    print("C")

elif(jumsu>=60 and jumsu<70):
    print("D")

elif(jumsu>100 or jumsu<0):
    print("다시 입력해주세요")
else:
    print("F")