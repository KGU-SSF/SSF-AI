for i in range(1,6):
    for l in range(6-i):
        print(" ",end="") #end=""는 print의 줄바꿈 방지
    print("*"*i)
        

'''for i in range(1, 6):  
    print(" " * (6- i) + "*" * i)  ''' #젤쉬운 방법