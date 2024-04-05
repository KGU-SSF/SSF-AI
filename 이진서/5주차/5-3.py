def a1(x,y,z,t):
    return x+y+z+t

i1 = input()
n1 = list(map(int, i1.split()))

r1 = a1(*n1)



def a2(x,y,z,t):
    return x+y+z+t

i2 = input()
n2 = list(map(int, i2.split()))

r2 = a2(*n2)



def a3(x,y,z,t):
    return x+y+z+t

i3 = input()
n3 = list(map(int, i3.split()))

r3 = a3(*n3)


if r1 == 3:
    print("A")

elif r1 == 2:
    print("B")

elif r1 == 1:
    print("C")


elif r1 == 0:
    print("D")

elif r1 == 4:
    print("E")



if r2 == 3:
    print("A")

elif r2 == 2:
    print("B")

elif r2 == 1:
    print("C")

elif r2 == 0:
    print("D")

elif r2 == 4:
    print("E")



if r3 == 3:
    print("A")

elif r3 == 2:
    print("B")

elif r3 == 1:
    print("C")

elif r3 == 0:
    print("D")

elif r3 == 4:
    print("E")











