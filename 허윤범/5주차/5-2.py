a = int(input()) 

for i in range(a):
    print(" " * (a - i - 1), end="") #공백을 출력하고, 그 수가 점점 감소한다
    
    print("*", end="") #가운데 별을 출력한다
    
    if i > 0:
        for j in range(2 * i - 1):
            if j % 2 == 0: # 짝수일 때 공백, 홀수일 때 별을 출력한다
                print(" ", end="")
            else:
                print("*", end="")
                
    if i > 0:
        print("*", end="") #첫째줄 제외하고 별을 출력한다
    print() #줄바꿈