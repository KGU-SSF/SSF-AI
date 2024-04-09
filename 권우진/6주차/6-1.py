from collections import deque

queue = deque()


string = input("입력: ")

for ch in string:
    queue.append(ch)
    
ori_queue = queue.copy()
queue.reverse()

for i in range(len(queue)):
    if queue[i] == ori_queue[i]:
        chk = True
    else:
        chk = False

print(chk)