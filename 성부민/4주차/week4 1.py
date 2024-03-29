space = ' ' 
star = '*'
n = int(input()) 
for i in range(n, 0, -1): 
    print(space * (i - 1) + star * (n - (i - 1))) 
