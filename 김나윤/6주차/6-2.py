"""
동규가 0~9까지 적힌 카드를 내려놓는 게임을 하고있는데
기혁이가 옆에서 카드의 숫자를 세주고있다.
기혁이는 잘못된 수를 부를 때 마다 0을 말하고
가장 최근에 말한 카드를 지우게 한다.
동규는 이렇게 모든 카드를 내려놓은 후 그 카드에 적힌
숫자의 합을 구하려고 한다.
첫 번째 줄에 정수 K가 주어진다.
이후 K 개의 줄에 정수가 1개씩 주어진다. 
정수가 0일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.
"""

from collections import deque
dq = deque()

# K 입력받기
K = int(input("K 입력 : "))

# K번 반복
for i in range (0, K) :
    while True :
        num = int(input("카드 숫자 입력 : "))
        
        # 카드의 숫자는 0~9 조건
        if (num > 9 or num < 0) :
             print("잘못 입력했습니다")
        else :
             break
    
    # 숫자가 0인 경우 최근 카드 제거
    if (num == 0) :
        dq.pop()
    
    # 조건에 위배되지 않으면 데크에 추가
    else :
        dq.append(num)

# 데크의 합 구하고 출력하기
result = sum(dq)
print(result)