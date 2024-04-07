N = int(input())
star= "* "
space=" "

for i in range(N, 0 , -1):
    
    print(space *  (i -1), end=" ")
    print(star * (N-(i-1)))