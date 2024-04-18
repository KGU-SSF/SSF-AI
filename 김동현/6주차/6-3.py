a = int(input())
list = []

for i in range(a): #횟수 자체는 똑같으므로 a에 손댈 필요 없음
    list.append(int(input()))
list.sort() #리스트 오름차순 정렬

for i in range(a):
    print(list[i])