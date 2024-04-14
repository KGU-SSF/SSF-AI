N = int(input())  

ns = []  
for _ in range(N):
    n = int(input())  # 수 입력받기
    ns.append(n)  # 리스트에 수 추가

ns.sort()  # 입력된 수를 오름차순으로

for num in ns:  # 정렬된 수를 하나씩 출력
    print(num)
