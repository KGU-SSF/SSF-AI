N = int(input("수의 개수를 입력하세요. : "))
import random
def random_sequence(N):
    numbers = list(range(1, N+1))#1부터 N까지의 숫자를 랜덤으로 나열하기 위해 random_sequence 함수를 사용
    random.shuffle(numbers)#random.shuffle함수를 사용해서 리스트의 숫자들을 무작위로
    return numbers
result = random_sequence(N)
print(result)

result = sorted(result)#오름차순으로 정렬하기 위해 sorted(result) 함수를 사용

for result2 in result: #한줄마다 하나씩 출력
    print(result2)