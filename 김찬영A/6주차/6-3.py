N = int(input())
arr = []

for i in range(N):
    a = int(input())
    if a not in arr:  # 추가하려는 숫자가 이미 리스트에 있는지 확인
        arr.append(a)

arr.sort() # 리스트 오름차순 정렬

for i in arr: # arr의 각 요소를 반복적으로 접근하여 그 값을 변수 i에 할당
    print(i)
