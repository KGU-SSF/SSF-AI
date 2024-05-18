a = input()
b = len(a)
c = 0
d = 0
for i in range(b//2):
    if a[c] != a[b-1]: #b는 글자 개수이므로, 0부터 시작하는 토큰번호를 고려해야함
        d = d + 1
    c = c + 1
    b = b - 1
if d == 0:
    print("True")
else:
    print("False")