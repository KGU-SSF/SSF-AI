score = int(input("시험 점수를 입력하시오 :"))

if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 60 and score < 70:
    print("D")
elif score >= 0 and score < 60:
    print("F")
else:
    print("다시 입력해주세요")