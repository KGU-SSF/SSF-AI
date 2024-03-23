#1번문제
a = input("숫자1을 입력하세요")
b = input("숫자2를 입력하세요")
a = int(a)
b = int(b)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
#2번문제
x = input("시험 점수")
x = int(x)
if 90 <= x <= 100: print("A")
elif 80 <= x <= 89: print("B")
elif 70 <= x <= 79: print("C")
elif 60 <= x <= 69: print("D")
elif x >= 100 or x < 0: print("다시 입력해주세요")
else: print("F")
#3번문제
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = nums[::2]
print(c)
#4번문제
d = ["축구", "야구", "농구", "배구", "탁구"]
print(len(d))