#5주차 1번

ans = []
for i in range(5):
    ans.append(int(input()))

result = []
for i in ans:
    if i < 50:
        result.append(50)
    else:
        result.append(i)

score = sum(result) / len(result)

print(int(score))
