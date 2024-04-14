k= int(input())
cards=[]

for _ in range(k):
    o=int(input())
    if o==0:
        cards.pop()

    else:
        cards.append(o)

sum = 0
for i in range(len(cards)):
    sum = sum + cards[i]

print(sum)
