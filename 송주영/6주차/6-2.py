N = int(input("입력받을 숫자의 갯수를 입력하시오: "))

num = []
for _ in range(N): #숫자 입력
    a = int(input("숫자를 입력하시오: "))
    num.append(a) #리스트 저장

for i in range(N): 
    if num[i] == 0: #리스트의 특정값이 0일때
        for k in range(len(num)): #리스트를 순환하며 특정값인 경우 0으로 변경
            if num[k] == num[i-1]:
                num[k] = 0

s = sum(num) #합계 출력
print(s)