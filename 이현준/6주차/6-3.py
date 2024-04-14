N = int(input())

print("")                                       # 단순 줄바꿈

numbers = [int(input()) for _ in range(N)]

numbers.sort()                                  # 리스트 속 요소 오름차순으로 정렬

print("")                                       # 단순 줄바꿈

for i in range(len(numbers)) :                  # 오름차순으로 출력
    print(numbers[i])