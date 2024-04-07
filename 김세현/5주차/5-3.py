i=0
while i<31:
    a, b, c, d=map(int,input().split())
    if a+b+c+d==0:
        print("D")
    if a+b+c+d==1:
        print("C")
    if a+b+c+d==2:
        print("B")
    if a+b+c+d==3:
        print("A")
    if a+b+c+d==4:
        print("E")
    i=i+1
