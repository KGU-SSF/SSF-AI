#3주차 최재우 과제

#1번

a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

#2번

a = int(input("점수 입력 > "))
if a > 100 or a < 0:
  print("다시 입력해주세요")
elif a >= 90:
  print("A")
elif a >= 80:
  print("B")
elif a >= 70:
  print("C")
elif a >= 60:
  print("D")
else:
  print("F")

#3번

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[0::2])

#4번

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

