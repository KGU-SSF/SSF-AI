k = int(input("숫자를 입력하시오 : "))

lis = []

for i in range(k):
    num = int(input("숫자를 입력하시오 : "))
    if num == 0:
        lis.pop()
    else:
        lis.append(num)

a = sum(lis)

print(a)