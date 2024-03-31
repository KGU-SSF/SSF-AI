N = int(input("정수를 입력하시오 : "))


for i in range(N):
    print(str("*"*(i+1)).rjust(N))