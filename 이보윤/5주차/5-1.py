a = int(input("준서의 성적을 입력하세요: "))
b= int(input("이다의 성적을 입력하세요: "))
c = int(input("홍다의 성적을 입력하세요: "))
d = int(input("우진의 성적을 입력하세요: "))
e = int(input("우현의 성적을 입력하세요: "))


if a< 50:
    a = 50
if b< 50:
    b= 50
if c < 50:
    c = 50
if d< 50:
    d= 50
if e < 50:
    e = 50


k = (a+b + c + d + e) // 5


print("평균 성적은", k, "입니다.")