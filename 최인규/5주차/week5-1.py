# 학생들의 성능을 저장할 리스트 초기화
pf_list = []

# 5명의 학생 성능 입력 받기
for _ in range(5):
    pf = int(input())
    # 성능이 50점 미만이면 50점으로 처리
    if pf < 50:
        pf = 50
    pf_list.append(pf)

# 평균 성능 계산
avg = sum(pf_list) / len(pf_list)

# 평균 성능 출력
print(int(avg))
