N = int(input())

nums =[]
for _ in range(N) :
    num = int(input())
    nums = nums + [num]
    
    nums.sort()
    for num in nums:
        print(num)