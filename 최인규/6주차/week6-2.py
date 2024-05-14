from collections import deque

k = int(input()) # 사용자로부터 정수 k를 입력받음

queue = deque() # deque 객체를 생성하여 queue 변수에 할당

for i in range(k): 
    a = int(input()) 
    
    if a == 0: 
        
        if queue: # queue가 비어있지 않다면
            queue.pop() # queue의 마지막 요소를 제거
            
    else: 
        queue.append(a) # queue에 a를 추가
print(sum(queue)) # queue의 모든 요소의 합을 출력
