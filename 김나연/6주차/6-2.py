K = int(input())         # 카드의 개수를 입력받는다
cards = []               # 카드를 담을 리스트
for i in range(K):       # K개의 카드를 입력 받는다
  card = int(input())
  cards.append(card)
  
stack = []          # 말한 수를 저장할 스택 
total_sum = 0       # 카드에 적힌 숫자의 합
for card in cards:
  if card == 0:                  # 만약 잘못된 수를 말했으면
    last_card = stack.pop()      # 가장 최근에 말한 카드 제거 
    total_sum -= last_card       # 해당 카드에 적힌 숫자를 합에서 뺀다
  else:
    stack.append(card)        # 스택에 현재 카드 추가
    total_sum += card         # 카드에 적힌 숫자를 합에 더해준다
print(total_sum)              # 숫자의 합 출력 