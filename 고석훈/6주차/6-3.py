N = int(input())
n = []
for _ in range(N):
    num = int(input())
    n.append(num)
n.sort()


for num in n:
    print(num)