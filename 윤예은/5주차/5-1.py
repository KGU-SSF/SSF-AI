scores=[] #빈 리스트 생성
for _ in range(5): #for문을 사용해 5번 입력받음
    score=int(input())

    if (score>100 or score<0): #조건문 세 개를 사용해 입력된 성능이 조건에 충족하는지 확인
        print('성능은 모두 0이상 100이하의 정수여야 합니다.')
        break #오류 메세지를 출력하고 프로그램 중단

    elif (score%5!=0):
        print('모든 성능은 5의 배수여야 합니다.')
        break
    
    elif (score<50):
        score=50

    scores.append(score) #모든 조건을 충족한 성능을 scores 리스트에 추가함

average_score=sum(scores)//5 #평균 성능도 정수이므로 모든 성능의 합을 5로 나눈 몫을 평균으로 함

print(average_score) #출력