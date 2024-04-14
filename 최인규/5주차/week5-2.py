# 사용자로부터 정수 n을 입력받음
n = int(input())

# 1부터 n까지 반복
for i in range(1, n+1): 
    
    # n에서 현재 반복 횟수를 뺀 만큼 공백을 출력
    for j in range(n-i):
        print(' ', end='')
        
    # 현재 반복 횟수만큼 '*'을 출력
    for j in range(i):
        print('* ', end='')
        
    # 한 줄을 다 출력한 후 다음 줄로 넘어감
    print()