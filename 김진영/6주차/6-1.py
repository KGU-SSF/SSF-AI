a = input("입력하시오 : ")
r = True
for i in range(len(a)//2):
    if a[i] != a[-1-i]:
        r = False
        break
    print(r)