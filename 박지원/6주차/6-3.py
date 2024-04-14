N = int(input())
numbers=[]
for _ in range(N):
    number = int(input())
    numbers.append(number)
    
numbers.sort()
for number in numbers :
    print(number)    