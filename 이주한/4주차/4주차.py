# 1번

N = int(input("숫자를 입력하세요."))

for i in range(1, N+1):
  print(" "*(N-i), "*"*i)

# 2번

price_list = [32100, 32150, 32000, 32500]

for i in range (4):
  print(price_list[i])

# 3번

def print_coin():
  print("비트코인")

print_coin()

# 4번

for i in range(1,11):
  print(i*3)

# 5번

T = tuple(i for i in range (1, 100) if i % 2 == 0 )

print(T)



