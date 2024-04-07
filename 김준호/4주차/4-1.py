a = int(input("숫자를 입력하세요: "))
b=a
for i in range(b):
    print(" " * (b - (i+1)), end="")
    print('*' * (i+1))
    