#4-1
N = int(input())
for a in range(1, N+1):
    print(" " * (N-a)+ "*" * a)   



#4-2
price_list = [32100, 32150, 32000, 32500]
for a in range(len(price_list)):
    print(price_list[a])



#4-3
def print_coin():
    print("비트코인")

print_coin()



#4-4
for a in range(0,31,3):
    print(a)



#4-5
a = tuple(range(2,100,2))
print(a)
