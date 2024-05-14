a = input()
a = a.lower()
b = True

if a != a[::-1]:
  b = False

print(b)