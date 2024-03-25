##아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range사용##

price_list = list(map(int, input().split()))
s = len(price_list)

for i in range(s):
    print(price_list[i])