a=int(input("원하는 별의 갯수는? :"))

for i in range(1,a+1):
    print(" "*(a-i)+"*"*i)