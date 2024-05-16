#for문, 비교 연산자, 큰 값 스택에 저장, while pop
#스택보다 큐가 더 적절 
from collections import deque

queue = deque()
n = int(input("입력할 정수의 개수: ")) 

a = []
for i in range(n):
    num = int(input("정수를 입력하세요: "))
    a.append(num)

a.sort()

for num in a:
    queue.append(num)

while queue:
    print(queue.popleft())
