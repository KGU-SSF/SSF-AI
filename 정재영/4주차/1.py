N = int(input("정수를 입력하시오: "))

for i in range(1,N + 1):
    print(" " * (N - i) + "*" * i)