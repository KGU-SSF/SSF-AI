a = int(input("준서의 성능을 입력하시오(0점 이상 100점 이하인 5의 배수):" ))
if a >= 50:
    a = a
else:
    a = 50      
  
b = int(input("이다의 성능을 입력하시오(0점 이상 100점 이하인 5의 배수):" ))
if b >= 50:
    b = b
else:
    b = 50

c = int(input("홍다의 성능을 입력하시오(0점 이상 100점 이하인 5의 배수):" ))
if c >= 50:
    c = c
else:
    c = 50 

d = int(input("우진의 성능을 입력하시오(0점 이상 100점 이하인 5의 배수):" ))
if d >= 50:
    d = d
else:
    d = 50 

e = int(input("우현의 성능을 입력하시오(0점 이상 100점 이하인 5의 배수):" ))
if e >= 50:
    e = e
else:
    e = 50

average = (a + b + c + d + e) // 5
print(average)    