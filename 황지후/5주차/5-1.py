gra = []


gra.append(int(input("첫번째 성능을 입력하시오 : ")))
gra.append(int(input("두번째 성능을 입력하시오 : ")))
gra.append(int(input("세번째 성능을 입력하시오 : ")))
gra.append(int(input("네번째 성능을 입력하시오 : ")))
gra.append(int(input("다섯번째 성능을 입력하시오 : ")))

for i in range (5):
    if gra[i] <= 50:
        gra[i] = 50

result = 0

for i in range(5):
    result += gra[i]

result = result/5

print (result)


    