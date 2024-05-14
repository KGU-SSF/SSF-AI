sum=0               #변수 초기화

for i in range(5):  #5번 반복 입력
    score=int(input("5명의 성적을 입력하시오: "))
    if score <= 50:
        score=50    #50점 이하일때 50점으로 정의
    sum+=score      
avr=sum//5          #평균 내리기
print("평균:%d" % avr)