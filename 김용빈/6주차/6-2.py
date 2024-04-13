# K = int(input("카드의 개수:"))

# stack = []
# for i in range(K):
#     num = int(input("카드에 적힌 숫자: "))
#     num = (1,10)
#     if num == 0:
#         stack.pop()
#     else:
#         stack.append(num)
        
# total_sum = sum(stack)

# print(total_sum)

stack = []  # 카드를 저장할 스택 초기화

for _ in range(10):  # 0부터 9까지의 카드를 내려놓음
    num = int(input("숫자를 부르세요: "))  # 옆에서 숫자 부르기
    while num < 0 or num > 9:  # 0부터 9까지의 숫자가 아닌 경우
        print("잘못된 숫자입니다. 다시 부르세요.")
        num = int(input("숫자를 부르세요: "))
    
    if num == 0:
        if stack:  # 스택이 비어있지 않은 경우에만 실행
            stack.pop()  # 가장 최근에 말한 카드를 지움
    else:
        stack.append(num)  # 올바른 숫자인 경우 카드를 스택에 추가

# 모든 카드를 내려놓은 후 스택에 남아 있는 카드의 숫자들의 합 계산
total_sum = sum(stack)

print("내려놓은 카드의 숫자의 합:", total_sum)  # 결과 출력
