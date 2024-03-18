#2번
'''
시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D,
나머지 점수는 F를 출력하는 프로그램을 작성하시오.
(100보다 큰수, 0보다 작은 수일 때는 “다시 입력해주세요” 출력)
'''

score = int(input("점수를 입력하시오: "))

if 100 >= score >= 90:
    print("A")
elif 89>= score >= 80:
    print("B")
elif 79 >= score >= 70:
    print("C")
elif 69 >= score >= 60:
    print("D")
elif score > 100 or score < 0:
    print("다시 입력해주세요")
else:
    print("F")