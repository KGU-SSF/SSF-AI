#4주차 1번
a=int(input("숫자를 입력하시오. : "))

for i in range(1,a+1):
    print(" " * (a-i) + "*" * i)

#4주차 2번
price_list = [32100,32150,32000,32500]
for i in range(4):
    print(3-i, price_list[i])

#4주차 3번
def print_coin():
    print("비트코인")

#4주차 4번
for num in range(3,31,3):
    print(num)

#4주차 5번
a = tuple(range(2,100,2))
print(a)