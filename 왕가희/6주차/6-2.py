def card_sum(cards):
    stack = []
    for card in cards:
        if card == 0:
            stack.pop()
        else:
            stack.append(card)
    return sum(stack)

K = int(input("카드의 수를 입력하세요: "))
cards = []
for i in range(K):
    card = int(input("카드 숫자를 입력하세요: "))
    cards.append(card)

result = card_sum(cards)
print("카드에 적힌 숫자의 합은:", result)
