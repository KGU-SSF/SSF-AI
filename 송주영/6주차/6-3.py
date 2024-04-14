N = int(input("숫자를 입력하시오: "))

num = []
for _ in range(N): #반복문으로 숫자 N개 입력
    number = int(input("숫자를 입력: "))
    num.append(number)

num.sort() #오름 차순으로 변경

for number in num: #정리된 리스트 차례대로 출력
    print(number)