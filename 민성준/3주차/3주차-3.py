nums = list(map(int,input("정수들을 입력하시오 : ").split()))

b = list()

for i in nums:
    if i % 2 == 1:
        b.append(i)

print(b)