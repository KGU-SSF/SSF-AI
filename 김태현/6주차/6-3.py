#6주차 3번 오름차순 정렬
queue = []
K = int(input())

for _ in range(K):
    qu = int(input())       # qu 값을 입력받아 queue에 저장
    queue.append(qu)
    
result = sorted(queue)             #배열의 값 오름차 순으로 정리해주는 함수 사용

print(result)