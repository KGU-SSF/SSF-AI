a = int(input())
b= []
for i in range(1, a+1):
    line = " "*(a-i)
    for p in range(i):
        line += "* "
    b.append(line)
    print(line)