#3주차 과제

#1
A= int(input ())
B= int(input())

print(A+B,A-B,A*B,A/B,A%B)

#2
score=(int(input))
while (score < 0 or score >100):
    print("점수를 입력해주세요")
    if (90<= score<=100): print("A")
    elif(80<= score <=89): print("B")
    elif(70<= score <= 79): print("C")
    elif(60<= score <= 69): print("D")
    else: print("F")
    
    #3
    num=[1,2,3,4,5,6,7,8,9,10]
    print(num[0::2])
    
    #4
    cook=["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","쏘세지","라면","팥빙수","김치전"]
    print(len(cook))



