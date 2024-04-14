n = int(input("N 입력 : "))
list = []
sum = 0

for i in range (0,n):
    inp = int(input()) 
    if(inp == 0):
        list.pop()
    elif(inp >= 10 or inp < 0):
        i-1
    else:
        list.append(inp)
for i in range (0,len(list)):
    sum += list[i]
print()
print(sum)