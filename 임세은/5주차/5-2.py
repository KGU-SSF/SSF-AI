n=int(input("숫자를 입력하시오:"))  #별의 높이를 입력

for i in range(n):
    
    for k in range(n-1,i,-1):   #공백출력
        print(" ",end="")

    for j in range(1,i+2):  #별의 갯수 출력
        print("* ",end="")
    print() #줄바꿈