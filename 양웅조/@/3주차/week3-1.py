x = int(input("자연수를입력하세요"))
y = int(input("자연수를 입력하세요"))

if x <= 0:
    print("자연수로 입려하세요")
if y <= 0:
    print("자연수로 입력하세요")

else:
    print("합=", x + y)
    print("차=", x - y)
    print("몫=", round(x / y))
    print("나머지=", x % y)