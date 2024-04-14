stack = []

n = int(input())

for i in range(0,n) : 
    value = int(input())
    stack.append(value)
    
for i in range(0,n) :
    for j in range(i, n) :
        if(stack[i]>=stack[j]) :
            t = stack[i]
            stack[i] = stack[j]
            stack[j] = t
            
print(" ")
for k in range(0,n) :
    print(stack[k])