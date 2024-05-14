
n = int(input("수의 개수를 입력하세요: "))
numbers = []

for _ in range(n):
    numbers.append(int(input()))


numbers.sort() #오름차순 정렬

for number in numbers:
    print(number)

