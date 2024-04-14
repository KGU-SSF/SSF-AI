a = int(input("몇개의 숫자를 입력하실건가요? : "))
number = []
for i in range(0, a):
    b = int(input())
    number.append(b)
number.sort()
print(number)