

students= ["준서","이다","홍다","우진","우현"] #학생들 이름 배열로 저장
scores={}# 성적 입력받을 딕셔너리 지정

for student in students:# students 배열안에 있을 떄 까지 반복문 돔
    score = int(input(f"{student}의 성적을 입력하세요:"))#딕셔너리 안에 점수 입력
    scores[student] = score

for student ,score in scores.items():# value: student,score: key 에 이름과 점수 있을떄 까지 반복문 돔
    print(f"{student}: {score}점")# 이름과 점수 출력
    
for key,value in scores.items():#value: student,score: key 에 이름과 점수 있을떄 까지 반복문 돔
    if value >=50:#50점 이상이면 그대로 점수 인정
        pass
    elif value < 50: #50점 미만이면 전 점수와 상관없이 그대로 50점으로 인정
        scores[key] =50
        
average = sum(scores.values())/ len(scores) # 딕셔너리 value에 있는 모든 점수 더 한후 그 길이만큼 나누어서 평균 구한 후 average 변수에 저장
print("{:.2f} 점".format(average))# format 형식이용해서 평균점수 출력
        
        
        
    




