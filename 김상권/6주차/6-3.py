from collections import deque

N = int(input("숫자를 입력하세요 :" ))

numbers = deque()

print(N)

for _ in range(N):
    num = int(input())
    numbers.append(num)


for num in sorted(numbers):
    print(num)
    