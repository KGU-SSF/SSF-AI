# 1번 과제
num1 = int(input())
num2 = int(input())

print(num1+num2, num1-num2, num1*num2, int(num1/num2), int(num1%num2))

# 2번 과제
while True:
  score = int(input("시험 점수를 입력하세요: "))

  if score > 100 or score < 0:
    print("다시 입력해주세요.")
    continue

  if 90 <= score <= 100:
    print("A")
  elif 80<= score <=89:
    print("B")
  elif 70<= score <=79:
    print("C")
  elif 60<= score <=69:
    print("D")
  else:
    print("F")

  break

# 3번 과제
nums = [1,2,3,4,5,6,7,8,9,10]

print(nums[::2])

# 4번 과제
cook=["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","소세지","라면","팥빙수","김치전"]
print(len(cook))

