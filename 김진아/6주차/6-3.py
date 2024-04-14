n = int(input())

nums = []

for i in range(n):
    num=int(input("숫자를 입력하시오 : "))
    
    nums.append(num)

a = sorted(nums)

print(a)