K = int(input("카드의 개수를 입력해라: "))

cards = []
total_sum = 0

for _ in range(K):
    num = int(input())
    
    if num == 0:
        removed_card = cards.pop()
        total_sum -= removed_card
    else:
        cards.append(num)
        total_sum += num

print("카드에 적힌 숫자의 합:", total_sum)