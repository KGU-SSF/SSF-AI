from collections import deque

queue = deque()

n = int(input("입력: "))

for i in range(n):
    queue.append(int(input("숫자 입력: ")))
    
for i in range(len(queue)):
    max = i
    for j in range(i + 1, len(queue)):
        if queue[max] < queue[j]:
            max = j
    tmp = queue[max]
    queue.remove(queue[max])
    queue.appendleft(tmp)

for i in range(len(queue)):
    print(queue[i])