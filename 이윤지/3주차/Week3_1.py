import sys

A, B = map(int, sys.stdin.readline().split())
print(A+B, A-B, A*B, int(A/B), A%B)