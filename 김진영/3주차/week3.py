#1
a = int (input("변수를 입력하시오 : "))
b = int (input("변수를 입력하시오 : "))
print( a+ b, a-b, a*b , a//b, a%b)

#2
gr = int (input("점수를 입력하시오 : "))
if 90<= gr <= 100 :
    print("A")
else:
    if 80 <= gr < 90 :
         print("B")
    else:
        if 70<= gr < 80 :
            print("C")
        else:
            if 60<= gr <69 :
                print("D")
            else :
                if 0<= gr <60 :
                    print("F")                 
                else :    
                    print("다시 입력")
                    
#3
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v = nums[::2]
print(v)

#4
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
q=len(cook)
print(q)
