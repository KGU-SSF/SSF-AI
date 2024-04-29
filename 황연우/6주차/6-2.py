card = int(input())  
cards = []  

for _ in range(card):
    num = int(input())  
    if num == 0 and cards: 
        cards.pop() 
    else:
        cards.append(num)
print(sum(cards))