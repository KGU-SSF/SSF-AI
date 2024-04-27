n = int(input("숫자 입력 : "))

#범위 내의 경우
#1. 띄어쓰기
if 1 <= n <= 100:
    for i in range(1, n + 1):
        print(" " * (n - i), end="")

#2. 별 찍고 줄바꿈
        for j in range(1, i):
            print("* ", end="")
        print("*")

#예외
else:
    print("입력 범위 오류")
