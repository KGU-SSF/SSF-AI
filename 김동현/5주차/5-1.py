a = int(input())
while(a%5!=0 or a>100 or a<0):
    print("0이상 100이하인 5의 배수를 입력하세요")
    a = int(input())
if(a<50):
    a = 50
b = int(input())
while(b%5!=0 or b>100 or b<0):
    print("0이상 100이하인 5의 배수를 입력하세요")
    b = int(input())
if(b<50):
    b = 50
c = int(input())
while(c%5!=0 or c>100 or c<0):
    print("0이상 100이하인 5의 배수를 입력하세요")
    c = int(input())
if(c<50):
    c = 50
d = int(input())
while(d%5!=0 or d>100 or d<0):
    print("0이상 100이하인 5의 배수를 입력하세요")
    d = int(input())
if(d<50):
    d = 50
e = int(input())
while(e%5!=0 or e>100 or e<0):
    print("0이상 100이하인 5의 배수를 입력하세요")
    e = int(input())
if(e<50):
    e = 50
print((a+b+c+d+e)//5)