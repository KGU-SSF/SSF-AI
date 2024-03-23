#1
a=int(input("정수 1:"))
b=int(input("정수 2:"))
print(a+b, a-b, a*b, a//b, a%b)
#2
c=int(input("시험점수를 입력하세요:"))
if 90<=c<=100:
    print("A")    
else:
    if 80<=c<90:
        print("B")
    else:
        if 70<=c<80:
            print("C")
        else:
            if 60<=c<70:
                print("D")
            else:
                if 0<=c<60:
                    print("F")
                else:
                    print("다시 입력해주세요")
#3
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = nums[::2]
print(d)
#4
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
e = len(cook)
print(e)                
            