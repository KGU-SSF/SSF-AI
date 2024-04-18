N = int(input())
cards = []

for _ in range(N):
    card = int(input())
    cards.append(card)

num = []
total_sum = 0

for card in cards:
    if card != 0:
        num.append(card)
        total_sum += card

    else:
        if num:
            removed_card = num.pop()
            total_sum -= removed_card

print(total_sum)
