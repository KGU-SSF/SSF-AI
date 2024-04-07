a = int(input("점수를 입력하세요 : "))
b = int(input("점수를 입력하세요 : "))
c = int(input("점수를 입력하세요 : "))
d = int(input("점수를 입력하세요 : "))
e = int(input("점수를 입력하세요 : "))

if(a < 50):
    a = 50
if(b < 50):
    b = 50
if(c < 50):
    c = 50
if(d < 50):
    d = 50
if(e < 50):
    e = 50

f = (a+b+c+d+e)/5
print(f)
