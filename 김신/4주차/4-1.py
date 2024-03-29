a=int(input())
b=1
for i in range(1,a+1):
    print((b*'*').rjust(a))
    b+=1