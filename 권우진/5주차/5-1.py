# 1번

li_score = []
N = 5
total = 0

for i in range(5):
    li_score.append(int(input()))

for score in li_score:
    if score < 50:
        score = 50
    total += score

print(total // N)

