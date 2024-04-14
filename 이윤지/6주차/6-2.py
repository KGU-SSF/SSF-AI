K = int(input())

cards = []

for _ in range(K):
    n = int(input())

    if n == 0:
        cards.pop()

    else:
        cards.append(n)

print(sum(cards))