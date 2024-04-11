K = int(input())
cards = []
for i in range(K):
  card = int(input())
  cards.append(card)
  
stack = []
total_sum = 0 
for card in cards:
  if card == 0:
    last_card = stack.pop()
    total_sum -= last_card
  else:
    stack.append(card)
    total_sum += card 
print(total_sum)