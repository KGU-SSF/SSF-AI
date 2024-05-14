N = int(input())

numbers = [int(input()) for _ in range(N)]
for num in sorted(numbers):
    print(num)