stack = []
total = 0
n = int(input("뽑을 카드 수를 입력하세요:"))
for i in range(n):
    num = int(input())
    if num>=10 or num<0:
        num = int(input("0에서 9까지 숫자만 뽑을 수 있습니다:"))
    if num == 0:
        stack.pop()
        continue
    stack.append(num)
for j in range(len(stack)):
    total = total + stack[j]
print (total)