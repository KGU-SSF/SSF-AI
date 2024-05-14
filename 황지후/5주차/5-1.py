gra = []#빈 리스트 지정

#학생 다섯명의 성능 리스트에 각각 입력하기
gra.append(int(input("첫번째 성능을 입력하시오 : ")))
gra.append(int(input("두번째 성능을 입력하시오 : ")))
gra.append(int(input("세번째 성능을 입력하시오 : ")))
gra.append(int(input("네번째 성능을 입력하시오 : ")))
gra.append(int(input("다섯번째 성능을 입력하시오 : ")))

#리스트에 입력한 각각의 성적에서 50 이하는 50점으로 고정
for i in range (5):
    if gra[i] <= 50:
        gra[i] = 50

#출력을 위한 변수 지정
result = 0

#리스트 내에 존재하는 각각의 값을 변수에 더하기
for i in range(5):
    result += gra[i]

#리스트를 5로 나눠 평균내기
result = result/5

#출력
print (result)


    