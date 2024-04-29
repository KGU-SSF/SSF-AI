from collections import deque

word = input()

queue = deque()

ox = True

for i in range(len(word)):
    queue.append(word[i])

for j in range(len(word)):
    if queue[j] != queue[-1-j]:
        ox = False
        break

print(ox)