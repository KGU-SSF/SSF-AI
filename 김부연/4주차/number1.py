number = int(input("숫자를 입력해주세요:"))

for i in range(number):
    print(" " * (number - (i+1)), end="")# 공백을 먼저 출력해야 함,공백의 갯수 = number-라인 번호, 별의 갯수  = 라인번호,end="" 줄 띄우기 위함
    print('*' * (i+1))
