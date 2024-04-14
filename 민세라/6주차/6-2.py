n = int(input())
li = []
for _ in range(n):
    k = int(input())
    if(k == 0):
        li.pop()
    else:
        li.append(k)
result = 0

for i in li:
    result += i
print(result)