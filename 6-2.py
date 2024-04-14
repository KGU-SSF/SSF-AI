k = int(input("카드의 수를 입력하시오: "))      #카드의 수를 입력받음 
cards = []                   
for i in range(k):       #입력된 카드 수만큼 반복하여 각 카드의 값을 입력받음
  card = int(input())   #카드의 값을 입력받음
  cards.append(card)   #카드의 값을 cards에 추가함
  
stack = []          #카드를 저장할 stack 추가
total_sum = 0       #카드의 총 합계를 저장할 변수를 초기화
for card in cards:
  if card == 0:                  
    last_card = stack.pop()      #stack에서 맨 위 카드를 꺼내서 last_card변수에 저장
    total_sum -= last_card     #총 합에서 꺼낸 카드의 값을 뺀다
  else:
    stack.append(card)        
    total_sum += card         #현재의 카드의 값을 총합에 더함
print(total_sum)    