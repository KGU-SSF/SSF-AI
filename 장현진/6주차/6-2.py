stack = []
a = int(input())
for i in range(a):
    b = int(input())
    if b != 0:
        stack.append(b)
    elif b == 0:
        stack.pop()
s = sum(stack)
print()         
print(s)
