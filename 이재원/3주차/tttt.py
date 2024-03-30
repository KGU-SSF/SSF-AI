#문제1
a=int(input("숫자1 입력\n"))
b=int(input("숫자2 입력\n"))
print(a+b,a-b,a*b,a/b,a%b)

#문제2
a=int(input("시험 점수"))
if 90<=a<=100:
    print("A")
elif 80<=a<=89:
    print("B")
elif 70<=a<=79:
    print("C") 
elif 60<=a<=69:
    print("D")
elif 0<=a<=59:
    print("F") 
else:
    print("다시 입력해주세요")

#문제3
a=[1,2,3,4,5,6,7,8,9,10]
print(a[0:1]+a[2:3]+a[4:5]+a[6:7]+a[8:9])

#문제4
a=["피자","김밥","만두",'양념치킨','족발','라면','김치만두','쫄면','쏘세지','팥빙수','김치전','파전']
print(len(a))
