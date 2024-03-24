n = input("리스트를 입력하시오 : ")
n = n.replace("[", "")
n = n.replace("]", "")
nums = n.split(", ")
a_nums =[]

for i in range(len(nums)):
    if int(nums[i]) % 2 == 1:
        a_nums.append(int(nums[i]))

print (a_nums)
