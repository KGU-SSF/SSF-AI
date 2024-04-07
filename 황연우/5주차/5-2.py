a=int(input("성능을 입력하시오: "))
b=int(input("성능을 입력하시오: "))
c=int(input("성능을 입력하시오: "))
d=int(input("성능을 입력하시오: "))
e=int(input("성능을 입력하시오: "))

if a<50:
    a = 50
if b<50:
    b = 50
if c<50:
    c = 50
if d<50:
    d = 50
if e<50:
    e = 50
    
print(int((a+b+c+d+e)/5))   

#a,b,c,d,e를 변수를 입력받는다
# if 조건문을 사용해서 입력받은 성능이 50보다 작으면 50이 저장될 수 있게 한다
# a,b,c,d,e의 값을 받은 후 5로 나누어 출력한다                  
        
    
