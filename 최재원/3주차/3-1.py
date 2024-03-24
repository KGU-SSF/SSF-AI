a, b= map(int,input().split()) #python input split의 경우는 문자열을 동시에 받는다!
#이를 위해 해야될것 !
#1.) a= int(a) 등으로 형변환!
#2. ) map 을 사용하여 정수로 변환 해주기! map(int,input().split())

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

# 파이썬은 scanf나 scanner 대신 input을 이용해 값을 받는다!