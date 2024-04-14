from collections import deque
queue = deque()
sum =0

for i in range(int(input())):
    num = int(input())
    if num == 0:
        queue.pop()
    else:
        queue.append(num)
    

for _ in range(len(queue)):
    sum += queue.pop()

print("---------")
print(sum)