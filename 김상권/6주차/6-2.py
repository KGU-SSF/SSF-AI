from collections import deque

K = int(input("숫자를 입력하세요 :" ))

cards = deque()

print(K)

for _ in range(K):
    num = int(input())
    if num == 0:
        cards.popleft()
    else:
        cards.append(num)

result = sum(cards)

print(result)
