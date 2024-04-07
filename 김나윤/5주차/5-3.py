"""
동규가 윷놀이를 한다.
윷놀이는 네 개의 윷짝을 던져서 배(0)와 등(1)이 나오는 숫자를 세어
도, 개, 걸, 윷, 모를 결정한다.
네 개 윷짝을 던져서 나온 각 윷짝의 배 혹은 등 정보가 주어질 때
도, 개, 걸, 윷, 모 중 어떤 것인지를 결정하는 프로그램을 작성하라.
첫째 줄부터 셋째 줄까지 각 줄에 각각 한 번 던진
윷짝들의 상태를 나타내는 네 개의 정수(0 또는 1)가
빈칸을 사이에 두고 주어진다.
첫째 줄부터 셋째 줄까지 한 줄에 하나씩 결과를
도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E로 출력한다.
"""


# 변수 선언
ar =[[0 for i in range(4)] for i in range(3)]
num = []
result = []
status = []

# 윷짝 입력 받기
for i in range(3) :
    num = input(str(i+1) + "번째 윷짝 입력 : ").split()
    ar[i] = list(map(int, num))

# 윷짝 상태 계산
for i in range(3) :
    result = sum(ar[i][:4])
    status.append(result)

# 도개걸윷모 판정
for i in range(3) :
    if (status[i] == 3) : # 도
        print("A")
    elif (status[i] == 2) : # 개
        print("B")
    elif (status[i] == 1) : # 걸
        print("C")
    elif (status[i] == 0) : # 윷
        print("D")
    elif (status[i] == 4) : # 모
        print("E")
    else :
        print("잘못 입력했습니다")