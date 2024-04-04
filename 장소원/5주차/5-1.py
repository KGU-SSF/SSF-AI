#1
num1 = int(input("점수 1 입력: "))
if num1 < 50 :
    num1 = 50
num2 = int(input("점수 2 입력: "))
if num2 < 50 :
    num2 = 50
num3 = int(input("점수 3 입력: "))
if num3 < 50 :
    num3 = 50
num4 = int(input("점수 4 입력: "))
if num4 < 50 :
    num4 = 50
num5 = int(input("점수 5 입력: "))
if num5 < 50 :
    num5 = 50
  
print((num1 + num2 + num3 + num4 + num5)//5)