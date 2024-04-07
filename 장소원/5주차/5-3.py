#3
a,b,c,d = input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)

e,f,g,h = input().split()
e=int(e)
f=int(f)
g=int(g)
h=int(h)

i,j,k,l = input().split()
i=int(i)
j=int(j)
k=int(k)
l=int(l)


if a + b + c + d == 0 :
    print("D")
else:
    if a + b + c + d == 1:
        print("C")
    else:
        if a + b + c + d == 2:
            print("B")
        else:
            if a + b + c + d == 3:
                print("A")
            else:
                print("E")
                
                
if e + f + g + h == 0 :
    print("D")
else:
    if e + f + g + h == 1:
        print("C")
    else:
        if e + f + g + h == 2:
            print("B")
        else:
            if e + f + g + h == 3:
                print("A")
            else:
                print("E")
                
if i + j + k + l == 0 :
    print("D")
else:
    if i + j + k + l == 1:
        print("C")
    else:
        if i + j + k + l == 2:
            print("B")
        else:
            if i + j + k + l == 3:
                print("A")
            else:
                print("E")
                
        
    