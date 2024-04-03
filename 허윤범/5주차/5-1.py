a = int(input("")) #점수가 50미만일 경우 50으로 설정
b = int(input(""))
c = int(input(""))
d = int(input(""))
e = int(input(""))

if a < 50:             
    a = 50
if b < 50:
    b = 50
if c < 50:
    c = 50   
if d < 50:
    d = 50   
if e < 50:
    e = 50
    
print((a+b+c+d+e)//5)

