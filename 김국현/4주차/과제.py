#1주차 과제

#1번
number = int(input())
for i in range(1,number+1):
    message = " "*(number-i)+"*"*i
    print(message)

#2번
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])

#3번
def print_coin():
    print("비트코인")

print_coin()

#4번
for i in range(3,31,3):
    print(i)

#5번
even = tuple(range(2,99,2))