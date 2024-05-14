N = int(input())

numbers = []
for _ in range(N):
    number = int(input())
    numbers.append(number)

sorted_numbers = sorted(numbers)

for num in sorted_numbers:
    print(num)