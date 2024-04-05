#N값을 받아오기
N = int(input("N값을 입력하시오 : "))

#N번만큼 *_로 피라미드층을 만들고 가운대에 정렬 후 각 층을 출력하기
for i in range (N):
    stars = ("* " * (i + 1)).center(N*2, " ")
    print(stars)