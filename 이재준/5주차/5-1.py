준서 = int(input())
이다 = int(input())
홍다 = int(input())
우진 = int(input())
우현 = int(input())  #수 입력받기
if 준서<50:
  준서=50
if 이다<50:
  이다=50
if 홍다<50:
  홍다=50
if 우진<50:
  우진=50
if 우현<50:
  우현=50
print(준서,이다,홍다,우진,우현)
a=준서+이다+홍다+우진+우현
b=a/5                      #나눗셈
print(b)
