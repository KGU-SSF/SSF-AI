k = int(input("시험 점수를 입력하세요: "))

if 90 <= k <= 100:
    print("A")
elif 80 <= k:
    print("B")
elif 70 <= k:
    print("C")
elif 60 <= k:
    print("D")
elif 0 <= k < 60:
    print("F")
else:
    print("다시 입력해주세요")