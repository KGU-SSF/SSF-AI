n = int(input()) #받을 수의 개수 정하기
a = []
for i in range(n):
    a.append(int(input())) #n개의 수 받을 동안 a 리스트에 추가
a.sort() # a 오름차순 정렬
print(a)