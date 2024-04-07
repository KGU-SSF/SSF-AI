ssf_list = ["준서", "이다", "홍다", "우진", "우현"]
sum = 0  #sum 초기화

for i in range(len(ssf_list)):
    score = int(input(f"{ssf_list[i]}의 시험점수를 입력하세요 : "))  # 각 학생의 점수 입력
    if score > 50:
        ssf_list[i] = score  # 입력 받은 점수로 요소 변경
    else:
        ssf_list[i] = 50  # 50점 미만이면 50으로 변경

# ssf_list의 점수를 합산
for score in ssf_list:
    sum += score

# 평균 계산
avg = sum / len(ssf_list)

# 평균 출력
print("평균 : %0.2f" % avg)