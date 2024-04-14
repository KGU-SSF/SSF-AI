N = int(input())

for i in range(1, N + 1):
    a = " " * (N - i)
    b = "*" * (2 * i - 1)
    print(a + b + a)