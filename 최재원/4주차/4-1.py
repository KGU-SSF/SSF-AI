num = int(input("별을 입력해주세요.: "))

for i in range(1, num + 1):
    print(" " * (num - i) + "*" * i)
    #파이썬에서는 문자열 출력시 C와 자바와 달리 직접 증감해주어야 
    #붙여서 나온다.
