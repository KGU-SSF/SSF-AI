#1번
'''
print("2개의 숫자를 입력하시오")
num1=int(input())
num2= int(input())

result1=num1+num2
print(result1)

result2=num1-num2
print(result2)

result3=num1*num2
print(result3)

result4=num1/num2
print(result4)

result5=num1%num2
print(result5)
'''

#2번
'''
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
'''

#3번
'''
nums=[1,2,3,4,5,6,7,8,9,10]
result=[]
for num in nums:
    if num%2!=0:
        result.append(num)

print(result)
'''

#4번
'''
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
a=len(cook)
print("리스트의 데이터의 갯수:", a)
'''