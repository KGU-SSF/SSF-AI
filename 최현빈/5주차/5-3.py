for i in range(3):                              #3번 반복
    a = list(map(int, input().split()))         #문자열 입력 공백 기준으로 분리하여 리스트 만들고 정수로 변환 list 변환 후 a에 저장
    if a.count(0) == 1:                         #도
        print("A")
    if a.count(0) == 2:                         #개
        print("B")
    if a.count(0) == 3:                         #걸
        print("C")
    if a.count(0) == 4:                         #윷
        print("D")
    if a.count(1) == 4:                         #모
        print("E")