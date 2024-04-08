K = int(input())  # 카드의 개수 입력

stack = []  # 스택 초기화
total = 0   # 카드에 적힌 숫자의 합을 저장할 변수

for _ in range(K):
    num = int(input())  # 각 카드에 적힌 숫자 입력
    
    if num == 0:
        removed = stack.pop()  # 가장 최근에 말한 카드를 스택에서 제거
        total -= removed  # 제거한 카드의 숫자를 합에서 뺌
    else:
        stack.append(num)  # 카드 숫자를 스택에 추가
        total += num  # 카드 숫자를 합에 더함

print(total)  # 카드에 적힌 숫자의 합 출력