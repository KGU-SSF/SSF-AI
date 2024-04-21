n = int(input())
a = []                     #빈 리스트 생성
for i in range(n):
    b = int(input())       #정수 입력 받아 b에 저장
    a.append(b)            #b를 a에 저장

a.sort()                   #리스트에 저장된 정수들을 오름차순으로 정리

for b in a:
    print(b)               #출력