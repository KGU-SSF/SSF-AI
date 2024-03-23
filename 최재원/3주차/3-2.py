
grade = int(input("점수를 입력하세요 : "))


if grade >= 90 and grade <= 100:
        print("A")
elif grade >= 80 and grade < 90: #파이썬 && 는 and
        print("B")
elif grade >= 70 and grade < 80:
        print("C")
elif grade >= 60 and grade < 70:
        print("D")
elif grade > 0 and grade < 60:
    print("F")
else:
    print("다시 입력해주세요.")
