N = int(input())
cards=[]
for _ in range(N):
    n =int(input())
    if(n == 0):
        cards.pop()
    else:
        cards.append(n)
result=0

for i in cards:
    result+= i
print(result)

        
    