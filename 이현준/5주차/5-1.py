sum = 0
n = 5

for _ in  range(n) :
    grade = int(input())
    
    if(grade < 0 or grade > 100 or grade % 5 != 0) :
        exit(0)
        
    elif(grade < 50):
        grade = 50
    
    sum += grade
    
avg = sum // n

print(avg)