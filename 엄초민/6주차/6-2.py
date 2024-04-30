N= int(input())
a= []

for _ in range(N):
    num = int(input())
    if num == 0:
        a.pop()  
    else:
        a.append(num)  

total = sum(a)

print(total)