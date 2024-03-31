while 1 :
    x = int(input("정수 x를 입력하시오."))
    y = int(input("정수 y를 입력하시오."))
    if x <= 0 and y <= 0 :
        print("자연수가 아닙니다")
        continue
    else :
        print("합", x + y)
        print("차", x - y)
        print("곱", x * y)
        print("나누기", x / y)
        print("나머지", x % y)
        break