#5주차 1번

ans = []
for i in range(5):
    ans.append(int(input()))

result = []
for i in ans:
    if i < 40:
        result.append(40)
    else:
        result.append(i)

score = sum(result) / len(result)

print(int(score))