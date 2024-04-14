from collections import deque #deque 라이브러리 선언
queue=deque()

a=int(input("숫자의 개수를 입력하세요"))
for i in range(a): #a만큼 반복
    b=int(input("숫자를 입력하세요"))
    if (b==0): #0이면 가장 최근 카드 삭제
        queue.pop()
    elif (b>=10): #10이상이면 0으로 취급
        queue.append(0)
    else:
        queue.append(b) #큐에 숫자 입력

sum =0
for j in range(len(queue)): #큐만큼 반복해서 sum에 합산
    sum+=queue[j]
print(sum)