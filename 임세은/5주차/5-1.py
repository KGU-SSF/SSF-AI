n=5
list1=[]
result=0

for i in range(n):
    num=int(input("숫자입력:"))
    list1.append(num)

for i in range(n):    
    if list1[i] <50:
        list1[i]=50
    result+=list1[i]

average=result//n
print("평균:",average)