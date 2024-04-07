a=map(int,input().split())
b=map(int,input().split())
c=map(int,input().split())
d=map(int,input().split())    #수 입력받기
sum=a+b+c+d                    #총합 값

if sum==0:
    print("D")
elif sum==1:
    print("C")
elif sum==2:
    print("B")
elif sum==3:
    print("A")
else:
    print("E")           #값에 따라 등급나누기
