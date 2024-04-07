matrix = [] #입력받을 리스트 선언
rows=3 #윷 던지는 횟수 입력
for i in range(rows):
    row = list(map(int, input().split())) #matrix 리스트의 요소인 row에 list함수로 요소 추가, map 함수로 정수의 요소만 입력받음, split함수로 공백 구분
    matrix.append(row) #row의 요소들 matrix에 입력

for yuts in matrix: #이중 리스트에서 등이 나온 횟수를 세기
    count = yuts.count(0)  
    if count == 1: #도
        print("A") 
    elif count == 2: #개
        print("B")
    elif count == 3: #걸
        print("C")
    elif count == 4: #윷
        print("D")
    else: #모
        print("E")