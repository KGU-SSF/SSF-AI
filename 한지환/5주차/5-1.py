#1번문제
a = int(input("준서 점수(5의 배수)"))
if a>100 or a<0: print("다시 입력")
if 0<=a<50: a = 50

b = int(input("이다 점수(5의 배수)"))
if b>100 or b<0: print("다시 입력")
if 0<=b<50: b = 50

c = int(input("홍다 점수(5의 배수)"))
if c>100 or c<0: print("다시 입력")
if 0<=c<50: c = 50

d = int(input("우진 점수(5의 배수)"))
if d>100 or d<0: print("다시 입력")
if 0<=d<50: d = 50

e = int(input("우현 점수(5의 배수)"))
if e>100 or e<0: print("다시 입력")
if 0<=e<50: e = 50

print(int((a+b+c+d+e)/5))



