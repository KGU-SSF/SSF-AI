from collections import deque

queue = deque()
count = int(input())

for i in range(count):
    temp = int(input())

    if temp != 0:
        queue.append(temp)

    if temp == 0:
        queue.popleft()

sum = 0

for i in range(len(queue)):
    sum += queue[i]

print(sum)

