# 1번
a = input()
b = input()

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

#2번
score = int(input("점수를 입력하세요: "))

if 100 >= score >=90:
    print('A')
elif 90> score >= 80:
    print('B')
elif 80 > score >= 70:
    print("C")
elif 70 > score >=60:
    print('D')
elif 60> score >= 0:
    print("F")
else:
    print("다시 입력하세요")

#3번
nums = [1,2,3,4,5,6,7,8,9,10]
for num in nums:
    if num %2 != 0:
        print(num)

#4번
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
cook_num = len(cook)
print(cook_num)