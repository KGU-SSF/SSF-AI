from collections import deque
n = int(input())
a = deque()
for i in range(n):
    b = int(input())
    if b == 0:
        a.pop()
    else:
        a.append(b)

print(sum(a))