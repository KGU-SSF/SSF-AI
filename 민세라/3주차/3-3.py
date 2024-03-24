nums = list(map(int,input().split(',')))
li = []

for i in range(len(nums)):
    if(nums[i] % 2 == 1):
        li.append(nums[i])
print(li)