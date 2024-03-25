a=int(input("입력해주세요"))

if a >= 90 and a <= 100 :
    print("A")

elif a >= 80 and a < 90 :
    print("B")

elif a >= 70 and a < 80 :
    print("C")

elif a >= 60 and a < 70 :
    print("D")

elif a > 100 or a < 0:
    print("다시 입력해주세요")

else :
    print("F")
