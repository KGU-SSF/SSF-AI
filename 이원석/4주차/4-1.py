i = int(input("별의 최대 갯수를 입력하세요: "))
star_row = ''
while i>0:
    while i>0:
        star_row = star_row + '*'
        i -= 1
        print("{0:>10}".format(star_row)) #최대 10개
i -= 1