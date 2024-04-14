from collections import deque


queue = deque()
total = 0

cnt = int(input("갯수 입력: "))
    
for i in range(cnt):
    tmp = int(input("숫자 입력: "))
    if tmp == 0:
        queue.pop()
    else:
        queue.append(tmp)
        
for i in range(len(queue)):
    total += queue[i]
print(total)
        

