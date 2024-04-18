a = int(input("정수를 입력하시오 : "))
b = []
for i in range(0,a):
    c=int(input())
    b.append(c)
b.sort()
for l in range(0,a):
    print(b[l])
