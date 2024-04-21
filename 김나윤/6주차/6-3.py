"""
N개의 수가 주어졌을 때 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
첫째 줄에 수의 개수 N이 주어진다. 두 번째 줄부터 N개의 줄에는 수가 주어진다.
수는 중복되지 않는다.
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""

# 리스트 초기화
num_list = []

# n 입력받기
n = int(input("n 입력 : "))

# n개의 수 입력받고 리스트에 추가
for i in range (0, n) :
    num = int(input("수 입력 : "))
    num_list.append(num)
    
# 중복 제거
num_list_data = list(set(num_list))

# 오름차순 정렬
num_list_data.sort()

# 출력
for i in num_list_data :
    print(i)