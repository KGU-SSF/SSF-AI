from collections import deque
q = deque()

a = int(input())
for i in range(a):
    q.append(int(input()))
    if q[-1] == 0: #가장 최근 토큰
        q.pop()
        if len(q) >= 2: #토큰이 1개일때에 pop이 두 번 작동하는걸 방지
            q.pop()
        
#for i in range(len(q)): #'len(q)-1'의 type는 int임
#    b =+ q[i] #sum이외에 다른 방법으로는 in 다음 인수를 'q'로 지정

print(sum(q))

#큐 자료구조의 동작은 파이썬 내 collections 모듈이
#제공하는 deuque 자료구조를 활용해 표현 가능
#deque는 데이터 입출력 속도가 리스트 보다 효율적
#또한 queue 라이브러리를 이용하는 것보다 간단
#popleft함수를 통해 데이터 삭제
#queue의 경우 원래 popleft만 되지만 문제의 조건을
#만족시키기 위해 pop사용