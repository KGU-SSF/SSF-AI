number = int(input())
for i in range(1,number+1):
    message = " "*(number-i)+"*"*i
    print(message)