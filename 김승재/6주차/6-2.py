stack = []

def push(value) :
    stack.append(value)

def pop() : 
    if stack :
      stack.pop()
    
n = int(input())

for i in range(n) :
    value = int(input())
    if value == 0:
        pop()
    else :
        push(value)  
sum = 0
for value in stack:
    sum += value

print(" ")
print(sum)