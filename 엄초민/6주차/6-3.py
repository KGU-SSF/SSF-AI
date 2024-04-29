N = int(input())

anum = []
for i in range(N):
    num = int(input())
    anum.append(num)

sorted_anum = sorted(anum)
for num in sorted_anum:
    print(num)