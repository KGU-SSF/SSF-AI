"""
예제를 보고 규칙을 유추한 뒤에 피라미드를 만들어 봅시다.
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
"""


# n 입력받기
n = int(input("정수 입력 : "))

# 변수 선언
n2 = 2 * n
star = '*'
blank = ' '
x = 0

# n만큼 반복
while n > x :
    print_star = star + (blank + star) * x
    print('{:^{n2}s}'.format(print_star, n2 = n2))
    x += 1