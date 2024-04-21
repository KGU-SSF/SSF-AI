def printStar(a):
    lng = 2*a-1

    for i in range(1,a+1):
        b = ""
        lng2 = 2*i-1
        emp = int((lng-lng2)/2) 
        for k in range(emp):
            b += " "
        for p in range(1,lng2+1):
            if(p%2 == 1):
                b += "*"
            else:
                b += " "
        for o in range(emp):
            b += " "
        print(b)

a = int(input())

printStar(a)