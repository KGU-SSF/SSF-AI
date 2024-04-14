K = int(input())

cads = []

for _ in range(K):
    num = int(input())
    if num == 0:
        cards = cards[:-1]
    else:
        cards += [num]
        
        print(sum(cards))