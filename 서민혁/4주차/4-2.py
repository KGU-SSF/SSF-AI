import re
a = input("입력 : ")
b = re.sub(r'[^0-9]', '', a)
c=[b[i:i+5] for i in range(0, len(b), 5)]
for i in range(1, len(c)+1):
    print(c[i-1])