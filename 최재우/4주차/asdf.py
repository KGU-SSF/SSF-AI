#1번

a= int(input())
for i in range(a):
    print(("*"*(i+1)).rjust(a))


#2번

price_list = [32100, 32150, 32000, 32500]

for i in range(4):
  print(price_list[i])


#3번

def 비트코인():
  print("비트코인")

비트코인()


#4번

for i in range(1, 31):
  if i%3 == 0:
    print(i)


#5번

a = tuple(range(2, 99, 2))
print(a)