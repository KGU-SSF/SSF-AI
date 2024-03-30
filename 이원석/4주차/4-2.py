price_list = []

for i in range(4):
    a = input("총 4개의 가격을 입력하세요: ")
    price_list.append(a)

for i in range(4):
    print(price_list[0])
    del price_list[0]