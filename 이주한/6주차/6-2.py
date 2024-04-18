from collections import deque


queue = deque()
total = 0


count = int(input("정수 K :"))
    

for i in range(count):
    temp = int(input("숫자:"))


    if temp == 0:
        queue.pop()
    else:
        queue.append(tmp)

        
for i in range(len(queue)):
    total += queue[i]
print(total)
