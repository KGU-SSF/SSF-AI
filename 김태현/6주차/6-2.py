#6주차 2번 스택
queue = []
K = int(input())

for _ in range(K):
    num = int(input()) 
    if num == 0:  #가장 최근 카드 삭제
        queue.pop()
    else:
        queue.append(num)  # 스택에 카드 추가

print(sum(queue))  #카드 합계 출력
