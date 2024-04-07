a = list(map(int,input("배가 나오면 0을, 등이 나오면 1을 띄어쓰기로 구분해서 입력해주세요.").split()))
a.sort()
while a[0] > 1 or a[1] > 1 or a[2] > 1 or a[3] > 1:
    print("각 토큰에는 0 혹은 1만 들어갈 수 있습니다.")
    a = list(map(int,input().split()))

b = a[0] + a[1] + a[2] + a[3]

if b == 1:
    print("C")
elif b == 0:
    print("D")
elif b == 2:
    print("B")
elif b == 3:
    print("A")
elif b == 4:
    print("E")
else:
    print("다시 입력하세요.")
    a = list(map(int,input().split()))