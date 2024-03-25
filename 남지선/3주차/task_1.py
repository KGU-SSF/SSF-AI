# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는
# 프로그램을 작성하시오.
# 입력예시 : 7 3
# 출력예시 : 10 4 21 2 1

num1,num2=input("숫자 입력:").split()

num1=int(num1)
num2=int(num2)

add=num1+num2
sub=num1-num2
mul=num1*num2
quo=num1//num2
rem=num1%num2

print("출력:",add, sub, mul, quo, rem)