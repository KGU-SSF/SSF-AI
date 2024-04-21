
card=[]

k=int(input("k:"))
for i in range(k):
    num=int(input(""))
    if num==0:
        o=card.pop()  
    else:
        card.append(num)
print("합:",sum(card))
