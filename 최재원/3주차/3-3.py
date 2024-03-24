nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#여기서 홀수만 슬라이싱을 통해 출력 

#파이썬에서의 for문은 for i in range로 쓴다!
print("출력 예시 : [", end = "")

for i in range(0, 10, 2):  #시작 끝 증감
    
    print("%d" % nums[i], end = "") # 한줄로 출력할려면 end =""사용
    if i == 9:
        break
    print(", ", end = "")
    
print("]")
