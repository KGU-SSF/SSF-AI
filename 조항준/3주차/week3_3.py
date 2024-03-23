print("리스트 요소 개수를 입력해주세요")
size = int(input())
print("숫자들을 입력해주세요")
nums = []
result = []

for i in range(0,size):
    nums.append(int(input())) 

for i in range(0,size):
    if(nums[i] % 2 != 0):
        result.append(nums[i:i+1])

print("결과")  
for i in range(0,len(result)):
    print(result[i])
    