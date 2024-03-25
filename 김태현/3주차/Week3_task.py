#1번
print("\n1번")
A,B=map(int, input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

#2번
print("\n2번")
while(1):
    Score=int(input())
    if(Score>100&Score<0):
        print( "다시 입력해주세요")
    elif(Score<=100&Score>=90):
        print("A")
        break
    elif(Score<90&Score>=80):
        print("B")
        break
    elif(Score<80&Score>=70):
        print("C")
        break
    elif(Score<70&Score>=60):
        print("D")
        break
    else:
        print("F")
        break

#3번
print("\n3번")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums)
print(nums [::2])

#4번
print("\n4번")
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(cook)
print(len(cook))

    
