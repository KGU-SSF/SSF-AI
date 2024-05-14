a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

e, f, g, h = input().split()
e = int(e)
f = int(f)
g = int(g)
h = int(h)

i, j, k, l = input().split()
i = int(i)
j = int(j)
k = int(k)
l = int(l)

if a + b + c + d == 1:
    print("c")
elif a + b + c + d == 2:
    print("B")
elif a + b + c + d == 3:
    print("A")
elif a + b + c + d == 4:
    print("E")
else:
    print("D")

if e + f + g + h == 1:
    print("C")
elif e + f + g + h == 2:
    print("B")
elif e + f + g + h == 3:
    print("A")
elif e + f + g + h == 4:
    print("E")
else:
    print("D")

if i + j + k + l == 1:
    print("C")
elif i + j + k + l == 2:
    print("B")
elif i + j + k + l == 3:
    print("A")
elif i + j + k + l == 4:
    print("E")
else:
    print("D")