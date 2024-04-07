for i in range(3):
    A= list(map(int,input().split()))
    E= A.count(0)
    
    if E==0:
        print("E")
    elif E==1:
        print("A")
    elif E==2:
        print("B")
    elif E==3:
        print("C")   
    else:
        print("D") 