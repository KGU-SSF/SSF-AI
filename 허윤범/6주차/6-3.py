N = int(input())  # 수의 개수 입력받는다

numbers = []  # 수를 저장할 리스트를 초기화한다

for _ in range(N):
    num = int(input())
    numbers.append(num)   #리스트에 수를 추가한다

numbers.sort()  # 오름차순으로 정렬한다

for num in numbers:   
    print(num)