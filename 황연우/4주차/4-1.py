N = int(input("N을 입력하시오: "))

for num in range(1,N+1):
    print(" "*(N-num))
    print("*"*num)