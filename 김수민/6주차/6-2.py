stack = []

num = int(input("원하는 카드 갯수는? :"))

for i in range(num):
    a = int(input())
    if a != 0:
        stack.append(a)
    else:
        stack.pop()

b = 0

for j in range(len(stack)):
    b = b + stack[j]

print(b)