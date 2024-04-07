#2. 피라미드 출력 프로그램
n=int(input("100이하의 자연수 입력 : "))
a=' '
b='*'
r=1
for i in range(1):
    print(a*(n-1)+b+a*(n-1))
    n-=1
while n!=0:
    print(a*(n-1)+(b+a)*r+b)
    n-=1
    r+=1