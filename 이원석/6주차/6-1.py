#한글자씩 읽어야 한다 , for, 앞에서 한번 읽고, 뒤에서 한번 읽고 다른 것을 만나면 리턴0, 같으면 리턴1
# 큐는 앞에서 꺼내고, 스택은 뒤에서 꺼낸다 큐와 스택에 한글자씩 넣고 하나씩 꺼내면서 둘이 같으면 1, 다르면 0

from collections import deque

s = input("단어를 입력하세요:")
list = list(s)
queue = deque()
stack = []
        
for i in list:
    queue.append(i)
    stack.append(i)

for i in range(len(s)):
    if queue.popleft() != stack.pop():
        o = 'False'
    else:
        o = 'True'
print('%s'%s)
print(o)