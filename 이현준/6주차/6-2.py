from collections import deque

def card_sum(K, numbers):
    queue = deque()
    
    for num in numbers:
        if num == 0:
            queue.pop()             # 가장 먼저 적은 숫자를 지움
        else:
            queue.append(num)       # 숫자를 큐에 삽입
    
    return sum(queue)               # 남아있는 숫자의 합

K = int(input())
numbers = [int(input()) for _ in range(K)]

if(any(nums > 9 or nums < 0 for nums in numbers)) :
    exit(0)

print(card_sum(K, numbers))