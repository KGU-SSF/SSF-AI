#3주차 과제

#1번
a = input()
b = input()

a = int(a)
b = int(b)

print(a+b, a-b, a*b, int(a/b), a%b)

#2번
score = int(input())

if(90<= score <= 100): print("A")
elif(80<=score<=89): print("B")
elif(70<= score <= 79): print("C")
elif(60<= score <= 69): print("D")
else: print("F")

#3번
num = [1,2,3,4,5,6,7,8,9,10]
print(num[0::2])

#4번
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))