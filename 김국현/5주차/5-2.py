num = int(input())

for i in range(1,num+1):
    temp = int((num*2 - 1) / 2)
    temp2 = temp - i + 1
    if i == 1:
        string = " "*temp + "*" + " "*temp
        print(string)
    if i % 2 == 0:
        string = ""
        if temp2 > 0: string += " "*(temp2)
        for j in range(i*2 - 1):
            if j % 2 == 0: string += "*"
            if j % 2 == 1: string += " "
        print(string)
    if i % 2 == 1 and i != 1:
        string = ""
        if temp2 > 0: string += " "*(temp2)
        for j in range(i*2 -1):
            if j % 2 == 0: string += "*"
            if j % 2 == 1: string += " "
        print(string)

