#5주차 2번

n = int(input("숫자를 입력하시오. : "))

for i in range(1,n+1):
    print(" " * (n-i) + "*" * (i*2-1))


