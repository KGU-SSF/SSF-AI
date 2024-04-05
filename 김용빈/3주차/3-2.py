# 시험 점수 입력 
score = int(input("시험점수를 입력하세요 : ")) 

# 점수에 따라 학점 부여 조건문 
if score >= 90 and score <= 100:
    grade = 'A'
elif score >= 80 and score <= 89:
    grade = 'B'
elif score >= 70 and score <= 79:
    grade = 'C'
elif score >= 60 and score <= 69:
    grade = 'D'
elif score < 0 or score > 100:
    print("다시 입력해주세요.")
    exit()
else:
    grade = 'F'

    
print("점수:", score, "학점:", grade)