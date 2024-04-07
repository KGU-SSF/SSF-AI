N = int(input())

if(N > 100 or N < 1) :              #범위를 벗어났을 때
    exit(0)

N = N + 1

for x in range(1, N) :              #피라미드 높이만큼 반복 & 여백 넣기
    print(" " * (N - x), end = "")
    
    for _ in range(x):
        print("* ", end="")         #별 넣기
        
    print("")                       #줄바꿈