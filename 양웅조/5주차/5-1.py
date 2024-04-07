junseo = int(input("준서의 성적을 입력하세요"))
eda = int(input("이다의 성적을 입력하세요"))
hongda = int(input("홍다의 성적을 입력하세요"))
woojin = int(input("우진이의 성적을 입력하세요"))
woohyun = int(input("우현이의 성적을 입력하세요"))

if junseo <= 50 :
    junseo = 50
if eda <= 50 :
    eda = 50
if hongda <= 50 :
    hongda = 50
if woojin <= 50 :
    woojin = 50
if woohyun <= 50:
    woohyun = 50

print ((junseo + eda + hongda + woohyun + woojin)/5)

#각 사람들의 성적을 받아오기 위해 int(input()) 사용 점수는 정수로 나오기 때문에 int사용
# 각각 점수가 50 미만이면 기초 스터디를 수강하기에 50점 출력 하도록 if 사용 50점 초과면 그대로 인정되니 각 합을 더해 5로 나누고 프린트
