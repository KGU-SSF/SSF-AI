N = int(input())
cards = []

for _ in range(N):
    card = int(input())
    cards.append(card)

right = []
total_sum = 0

for card in cards:
    if card != 0:
        right.append(card)
        total_sum += card

    else:
        if right:
            removed_card = right.pop()
            total_sum -= removed_card

print(total_sum)
