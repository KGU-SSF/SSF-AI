scores=0
for i in range(5):
    score=int(input("성적(5의 배수를 입력하세요):"))
    if 0 <= score < 50:
        score=50
    scores += score
average=int(scores/5)
print("결과=",average) #여기서 print("결과=",average) ,대신 + 쓰면 오류 문자열이 아니기 때문
    