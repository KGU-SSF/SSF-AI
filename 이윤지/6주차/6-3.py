N = int(input())

num = []

for _ in range(N):
    a = int(input())
    while(a in num):
        a = int(input("중복된 숫자는 입력할 수 없습니다.\n"))
    num.append(a)

print(set(num))