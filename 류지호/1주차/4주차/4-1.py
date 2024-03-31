a=int(input("줄의 갯수를 정하시오"))
for i in range(a+1):
    print(str("*"*i).rjust(a))