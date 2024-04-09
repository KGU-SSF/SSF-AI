#2
from collections import deque

a = int(input("총 입력할 수의 갯수를 적으세요: "))
b = deque()
sum = 0

for i in range(a):
    c=int(input("수: "))
    if c == 0:
        b.pop()
    else:
         b.append(c)

d = len(b)
        
for i in range(d): 
    e = b.pop()       
    sum += e
    
print(sum)
        
