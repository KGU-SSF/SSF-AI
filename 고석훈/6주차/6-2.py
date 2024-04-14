from collections import deque
K = int(input())
c = deque()

for _ in range(K):
    num = int(input()) 
   
    if num != 0:
        c.append(num)
    else:
        c.pop()


sum = sum(c)
print(sum)