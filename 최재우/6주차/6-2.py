a = int(input())
b = []

for i in range(a):
  c = int(input())
  if c == 0:
    b.pop()
  else:
    b.append(c)

d = sum(b)

print(d)