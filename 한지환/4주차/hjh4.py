#1번문제
a=input('숫자')
a=int((a))

for i in range(1,a+1):
    print(" "*(a-i)+'*'*i)      
    

#2번문제
price_list = [32100, 32150, 32000, 32500]
for i in range(0,4,1):
    print(price_list[i])

#3번문제
def print_coin():
    print("비트코인")

print_coin()
    
#4번문제
for i in range(3,31,3):
    print(i)

#5번문제
a = tuple(range(2,99,2))
print(a)

