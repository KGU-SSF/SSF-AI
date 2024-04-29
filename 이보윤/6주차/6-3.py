N = int(input())

numbers = []
for i in range(N):
    num = int(input())
    numbers.append(num)

numbers.sort()

for num in numbers:
    print(num)

for num in numbers:
    print(num, end='')