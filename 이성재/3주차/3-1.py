def cal(a, b):
    print(a+b, a-b, a*b, a//b, a%b)

A, B = input().split()
cal(int(A), int(B))
