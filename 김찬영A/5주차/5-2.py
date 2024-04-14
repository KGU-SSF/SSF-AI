N = int(input())

for i in range(N):
    for k in range(N-1-i): # i번째 줄에 N-1-i만큼의 공백 출력
        print(" ", end="")
    for j in range(i): # i번째 줄에 j가 i와 같아질 때까지 "* " 출력
        print("* ", end="")
    print("*") # 두 번째 코드에서 "* "를 여러번 출력하고 마지막에 "*"를 출력하고 줄을 넘김
