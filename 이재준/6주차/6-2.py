n = int(input())
cardsum = 0
prenumbers = []
for _ in range(n):
    a = int(input())
    if a != 0:
        cardsum += a
        prenumbers.append(a)  # 이전 숫자들을 기록
    else:
        lastnumber = prenumbers.pop()  # 가장 최근에 추가된 숫자 지우기
        cardsum -= lastnumber  # 합계에서 빼기
print(cardsum)
