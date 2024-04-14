#1
a = input("문자를 입력하세요: ")
b = True
for i in range(len(a)//2):
    if a[i] != a[-1-i]:
        b = False
        break
print(b)
