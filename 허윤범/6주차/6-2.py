K = int(input())  # 카드의 개수를 입력받는다

stack = []  # 스택을 초기화 한다
t = 0   

for _ in range(K):  #K번 반복한다
    num = int(input()) 
    
    if num == 0:
        d = stack.pop()  # 가장 최근에 말한 카드를 스택에서 제거한다
        t -= d  # 제거한 카드의 숫자를 합에서 뺸다
    else:
        stack.append(num)  # 카드 숫자를 스택에 추가한다
        t += num  # 카드 숫자를 합에 더한다

print(t)  # 카드에 적힌 숫자의 합 출력한다