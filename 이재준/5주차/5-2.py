n = int(input())
n= n + 1
 
for x in range(1, n) :               #1부터 n까지의 숫자 범위를 순회,x는 각 줄에서 별표의 개수
    print(" " * (n - x), end = "")   #공백을 출력,공백의 개수는 n - x
    for _ in range(x):               #x번 반복
        print("* ", end="")         
    print("") 
