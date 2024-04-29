N = int(input("숫자를 입력합시다!"))
a = list()                                   
for _ in range(N):                     #N 번 만큼 숫자 입력
    num = int(input())
    a.append(num)
a.sort()                           # 오름 차순으로 정렬
index=0
i = 0
while i < len(a)-1:                   
    if a[i] == a[i+1]:               # 현재 값이랑 다음 값이 같을경우
        del a[i]                     # 현재 값 삭제
    else:
        i+=1                         # 현재 값이랑 다음 값이 다를 경우 i 에 1 더함
        
for i in range(len(a)):
    print(a[i])
