# 0~9까지 10개의 카드가 있다.
# 스택에 카드의 수 하나씩 저장한다
# 잘못된 수를 부르면 0을 반환하고 스택 pop
# 10번 반복이 끝나면 스택의 남은 숫자의 합을 출력
# 첫 번째 줄에 정수 K = 내려놓을 카드의 수
# 똑같은 카드 중복 가능
stack = []
o = 0 
n = int(input("내려놓을 카드의 개수: ")) #정수형으로 K값 저장
for i in range(n): #K값 만큼 반복
    card_number = int(input("내려놓을 카드를 입력하세요: "))
    if card_number == 0:
        stack.pop()
        
    else:
        stack.append(card_number)
    print(stack)
while stack:  
    o += int(stack.pop())  
print(o)
