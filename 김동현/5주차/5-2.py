#a = int(input())
#for i in range(a+1):
#    if(i%2==0):
#        a = a+1
#5    print((" *"*i).center(a+2))
    
#print("*", end = '')

a = b = int(input())
b = b + 1
for i in range(a+1):
    print(" "*(b-1), end = ' ')
    print(("* "*i))
    b = b - 1