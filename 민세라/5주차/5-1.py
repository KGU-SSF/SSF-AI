li = []
for i in range(5):
    s = int(input())
    if(s < 50):
        s = 50
    li.append(s)

result = 0

for j in li:
    result += j

print(result // 5)