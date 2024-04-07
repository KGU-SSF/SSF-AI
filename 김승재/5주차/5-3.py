sum = [0, 0, 0]

for i in range(0,3) :
    a,b,c,d = map(int,input().split())
    if(a+b+c+d == 3):
        sum[i] = "A"
    elif(a+b+c+d == 2):
        sum[i] = "B"
    elif(a+b+c+d == 1):
        sum[i] = "C"
    elif(a+b+c+d == 0) :
        sum[i] = "D"
    elif(a+b+c+d == 4) :
        sum[i] = "E"

for(i) in range(3) :
    print(sum[i])