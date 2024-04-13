K = int(input("카드의 개수를 입력해라: "))

stack = []  

for _ in range(K):  
    num = int(input("숫자를 부르세요: "))  
    
    if num == 0:
        if stack:  
            stack.pop()  
    else:
        stack.append(num)  

total_sum = sum(stack)

print("내려놓은 카드의 숫자의 합:", total_sum)  