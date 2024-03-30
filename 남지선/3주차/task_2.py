# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D,
# 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# (100보다 큰수, 0보다 작은 수일 때는 “다시 입력해주세요” 출력)
# 입력예시 : 100
# 출력예시 : A

sco=int(input("점수를 입력해 주세요:"))

if sco>100 or sco<0 :
    sco=int(input("다시 입력해주세요:"))
if 100>=sco>=90:
    print("A")
elif sco>=80:
    print("B")
elif sco>=70:
    print("C")
elif sco>=60:
    print("D")
else:
    print("F")