n = int(input())
stack = []
for i in range(n):
    stack.append(int(input()))
stack.sort()
for j in range(n):
    print(stack[j])