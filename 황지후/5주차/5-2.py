N = int(input("N값을 입력하시오 : "))
for i in range (N):
    stars = ("* " * (i + 1)).center(N*2, " ")
    print(stars)