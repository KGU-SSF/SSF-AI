stack = []
total = 0

K = int(input()) 

for i in range(K):
    a = int(input())
    if (a > 9):
        continue
    if(a==0):
        stack.pop()
    else:
        stack.append(a)

total = sum(stack)
print(total)
