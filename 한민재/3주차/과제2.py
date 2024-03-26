a = int(input("점수 입력:"))
if a > 100 :
    print("점수 재입력")
elif 100>= a >=90:
    print("A")
elif 90 > a >=80:
    print("B")
elif 80 > a >=70:
    print("C")
elif 70 > a >=60:
    print("D")
elif 0 > a :
    print("점수 재입력")
else :
    print("F")