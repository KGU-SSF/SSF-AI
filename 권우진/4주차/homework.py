

# 1번
num = int(input("입력: "))

for i in range(num):
    for j in range(num - i - 1):
        print("-", end="")
    
    for k in range(i + 1):
        print("*", end="")
    print()

# 2번

strings = input("입력: ")
tmp_str = ""

for i in range(len(strings)):
    if strings[i] == "[":
        tmp_str = strings[i + 1: len(strings) - 1]
        break

tmp_li = tmp_str.split(", ")

for data in tmp_li:
    print(data)
    
# 3번
def print_coin():
    print("비트코인")

print_coin()
    
# 4번
li = []

for i in range(30):
    li.append(i + 1)

for data in li:
    if data % 3 == 0:
        print(data)
    
# 5번
li = []

for i in range(1, 100):
    if i % 2 == 0:
        li.append(i)
        
print(tuple(li))