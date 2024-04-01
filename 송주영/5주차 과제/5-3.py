# 결과 출력 함수
def determine_result(results):
    b = results.count(0) #배
    d = results.count(1) #등
    
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
results = []
for _ in range(3):
    line = input().split()
    results.append([int(x) for x in line])

# 결과 출력
for result in results:
    print(determine_result(result))