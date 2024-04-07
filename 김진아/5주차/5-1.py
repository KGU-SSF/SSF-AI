j = int(input())
i = int(input())
h = int(input())
uj = int(input())
uh = int(input())

if j < 50:
    j = 50
if i < 50:
    i = 50
if h < 50:
    h = 50
if uj < 50:
    uj = 50
if uh < 50:
    uh = 50

score = (j + i + h + uj + uh) // 5

print(score)