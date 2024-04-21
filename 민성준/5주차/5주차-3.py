result = []

def inputYut():
    a = list(map(int,input().split()))
    b = sum(a)
    if(b == 1):
        return "A"
    elif(b == 2):
        return "B"
    elif(b == 3):
        return "C"
    elif(b == 4):
        return "D"
    else:
        return "E"

for i in range(3):
    result.append(inputYut())

for k in result:
    print(k)
