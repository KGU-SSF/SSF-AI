a,b,c,d=list(map(int, input().split())) 
e,f,g,h=list(map(int, input().split()))
i,j,k,l=list(map(int, input().split()))

sum1=a+b+c+d
sum2=e+f+g+h
sum3=i+j+k+l

if sum1==0:
    print("D")
elif sum1==1:
    print("C")
elif sum1==2:
    print("B")
elif sum1==3:
    print("A")
else:
    print("E")
    
if sum2==0:
    print("D")
elif sum2==1:
    print("C")
elif sum2==2:
    print("B")
elif sum2==3:
    print("A")
else:
    print("E")
    
if sum3==0:
    print("D")
elif sum3==1:
    print("C")
elif sum3==2:
    print("B")
elif sum3==3:
    print("A")
else:
    print("E")