num = int(input("입력 : "))

if 1 <= num <= 100:
    for i in range(1, num + 1):
        print(" " * (num - i), end="")
        for j in range(1, i):
            print("* ", end="")
        print("*")
else:
    print("1부터 100까지의 숫자만 입력하세요.")