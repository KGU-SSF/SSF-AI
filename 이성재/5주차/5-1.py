lst = []
for _ in range(5):
    score = int(input())
    if score < 50:
        score = 50
    lst.append(score)

avg = sum(lst) // 5
print(avg)
