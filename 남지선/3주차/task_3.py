# 슬라이싱을 사용해서 홀수번째만 출력하라.
# 입력예시 : nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 출력예시 : [1, 3, 5, 7, 9]
nums=[]
nums=input("nums=").split()
nums=[int(k) for k in nums]
print("nums의 홀수 번째:",nums[::2])
