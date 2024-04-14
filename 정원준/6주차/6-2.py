from collections import deque
queue=deque()

a=int(input("숫자의 개수를 입력하세요"))
for i in range(a):
    b=int(input("숫자를 입력하세요"))
    if (b==0): #0이면 가장 최근 카드 삭제
        queue.pop()
    elif (b>=10): #10이상이면 0으로 취급
        queue.append(0)
    else:
        queue.append(b)

sum =0
for j in range(len(queue)):
    sum+=queue[j]
print(sum)