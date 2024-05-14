from collections import deque

word = input()

queue = deque()

for i in word :
    queue.append(i)             # queue 안에 입력받은 단어 삽입
    
reverse = deque(queue)          # reverse라는 큐에 queue 복사
reverse.reverse()               # 큐를 역순으로 변경
    
if(queue == reverse) :          # 입력받은 단어와 그 단어의 역순이 같은지 판단
    print("True\n")
else :
    print("False\n")