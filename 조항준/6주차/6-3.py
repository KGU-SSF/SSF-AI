n = int(input("N 입력 : "))
list = []
for i in range (0,n):
    inp = int(input()) 
    list.append(inp)
list.sort()
print()
for i in range (0,n):
    print(list[i])