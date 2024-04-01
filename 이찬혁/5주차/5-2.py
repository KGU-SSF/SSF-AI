x = int(input())
center = x 
for i in range(1,x+1):
    for j in range(1,2*x):
        if (i%2) == 0:
            if (abs(center - j)%2) == 1:
                if ((abs(center - j))) <= (i - 1):
                    print("*",end="")
                else:
                    print(" ",end="")
            else:
                print(" ",end="")
        else:
            if (abs(center - j)%2) == 0:
                if ((abs(center - j))) <= (i - 1):
                    print("*",end="")
                else:
                    print(" ",end="")
            else:
                print(" ",end="")
    print("")
        