k = int(input())
c = []

for i in range(k):
  n = int(input())
  if n == 0:
    c.pop()
  else:
    c.append(n)


print(sum(c))