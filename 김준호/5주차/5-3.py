stack  = []
for i in range(3):
    n = input()
    stack.append(n)
for j in range(3):
    if stack[j].count('0')==1:
        print("A")
    elif stack[j].count('0')==2:
        print("B")
    elif stack[j].count('0')==3:
        print("C")
    elif stack[j].count('0')==4:
        print("D")
    else: print("E")