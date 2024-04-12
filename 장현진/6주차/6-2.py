stack = []
a = int(input())#사용자로부터a 입력받음
for i in range(a):#0부터 a-1까지 반복
    b = int(input())#사용자로부터 b입력받음
    if b != 0:#b가 0이 아닌경우 stack에 추가
        stack.append(b)
    elif b == 0:#b가 0인경우 stack에서 맨 위값 제거
        stack.pop()
s = sum(stack)#반복문 종료 후 남아 있는값 합 s에 할당
print()         
print(s)
