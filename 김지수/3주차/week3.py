# 1
a=int(input("자연수 입력: "))
b=int(input("자연수 입력: "))

print(a+b, a-b, a*b, a//b, a%b)


# 2
score=int(input("점수를 입력하세요: "))

if score > 100 or score < 0 :
    print("다시 입력해주세요")
elif score >= 90 :
    print("A")
elif score >= 80  :
    print("B")
elif score >= 70:
    print("C")
elif score >= 60 :
    print("D")
else :
    print("F")


# 3
nums=[1,2,3,4,5,6,7,8,9,10]
print(nums[::2])


# 4
cook=["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))