def calculate_grade(score):
    if score > 100 or score < 0:
        return "다시 입력해주세요"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score = float(input("시험 점수를 입력하세요: "))
grade = calculate_grade(score)
print("등급은", grade, "입니다.")