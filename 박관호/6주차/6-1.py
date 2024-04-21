from collections import deque
org_queue = deque()

value = input("단어를 입력하세요")
print(value)
for i in value : 
    org_queue.append(i)
    
reversed_queue = deque(org_queue) 
reversed_queue.reverse()

if org_queue == reversed_queue : 
    print("True")
else :  
    print("False")