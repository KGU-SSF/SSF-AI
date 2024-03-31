#a = b = n = int(input())
#a = a - 1
#b = b - n + 1
#for i in range(1, n+1):
#    print(" "*a,"*"*b)
#    a = a - 1
#    b = b + 1

a = n = int(input())
for n in range(1, n + 1):
    print(("*"*n).rjust(a)) #문자열.rjust(자릿수, 채울 것) 오른쪽 정렬
    n = n + 1
    #commit 메세지 수정용