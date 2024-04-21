pyramid = ''
star = '*'
blank = ' '
a = int(input("입력: "))

# 피라미드 채우기
for i in range(1, a + 1):
    pyramid += blank * (a-i) + (star+blank)*i + blank * (a-i) + '\n'

print(pyramid)