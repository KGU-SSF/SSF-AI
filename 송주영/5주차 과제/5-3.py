# 결과 출력 함수
def determine_result(results): #규칙에 따라 결과 결정
    b = results.count(0) #배 0의개수 할당
    d = results.count(1) #등 1의개수 할당
    
    if b == 1 and d == 3:
        return "A"
    elif b == 2 and d == 2:
        return "B"
    elif b == 3 and d == 1:
        return "C"
    elif b == 4:
        return "D"
    elif d == 4:
        return "E"
    else:
        return "잘못된 입력!"

# 입력 받기
results = [] #리스트 생성
for _ in range(3):
    line = input().split()
    results.append([int(x) for x in line]) #리스트에 추가

# 결과 출력
for result in results:
    print(determine_result(result))