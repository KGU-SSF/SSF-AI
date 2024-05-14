num = int(input('숫자를 입력하시요. '))
for i in range(0, num) : 
    for j in range(i+1, num) : 
        print(" ", end="")
    for k in range(0, i+1) :
        print("* ", end="")
    print("")
    