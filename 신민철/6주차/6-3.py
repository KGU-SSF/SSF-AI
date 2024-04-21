from queue import PriorityQueue # 우선순위 큐
Q = PriorityQueue() # 우선순위 큐 생성
N = int(input("숫자 선택:")) # N개의 수 입력

for i in range(N): # N만큼 반복
    Q.put(input()) # 원소 추가
    


for i in range(N):
    print(Q.get()) # 원소를 오름차순으로 반환하는 특성 이용
   