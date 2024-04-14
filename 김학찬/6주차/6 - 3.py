from collections import deque

q = deque()
k = int(input())

for i in range(0,k):        # k만큼 반복함
    qu = int(input())       # qu 값을 입력받아 q 배열에 추가 시킴
    q.append(qu)
    
dab = deque(sorted(q))      #python에서 사용할 수 있는 배열 안에 값을 오름차 순으로 정리해주는 내장 함수 사용

print(dab)                  #오름차순으로 정리한 배열을 출력.