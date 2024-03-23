score = int(input("시험점수:"))

if score <= 100 and score >= 90:
    print('A')

elif score <= 89 and score >= 80:
    print('B')

elif score <= 79 and score >= 70:
    print('C')

elif score <= 69 and score >= 60:
    print('D')

elif score < 60:
    print('F')