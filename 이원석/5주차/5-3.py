import random
yut = [0,0,0,0]
print("윷을 3번 던집니다.")
for i in range(3):
    n=0
    for i in range(4):
        yut[i] = random.randint(0,1)
        if (yut[i]==1):
            n = n + 1
    print(yut)
    if(n==1):
        print("A")
    elif(n==2):
        print("B")
    elif(n==3):
        print("C")
    elif(n==4):
        print("D")
    else:
        print('E')
    