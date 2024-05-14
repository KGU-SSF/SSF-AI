from collections import deque

queue = deque()

max_num = int(input("숫자를 입력하세요 : "))
for i in range(max_num) : 
    num = (int(input()))
    if num == 0 : 
        queue.pop()
    else : 
        queue.append(num)

print(sum(queue))

