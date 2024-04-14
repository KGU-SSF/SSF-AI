from collections import deque          #collections 모듈에서 덱 import
n = int(input())
a = deque()                            #빈 덱 생성
for i in range(n):
    b = int(input())                   #정수 입력 받아 b에 저장
    if b == 0:
        a.pop()                        #입력 받은 정수가 0이면 덱의 마지막 요소 삭제
    else:
        a.append(b)                    #0이 아니라면 덱에 정수 추가

print(sum(a))                          #덱에 저장된 정수들의 합 출력