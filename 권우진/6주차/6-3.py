from collections import deque

queue = deque()

n = int(input("입력: "))

for i in range(n):
    queue.append(int(input("숫자 입력: ")))
    
for i in range(len(queue)):
    min = i
    for j in range(i + 1, len(queue)):
        if queue[min] < queue[j]:
            min = j
    tmp = queue[min]
    queue.remove(queue[min])
    queue.appendleft(tmp)

for i in range(len(queue)):
    print(queue[i])