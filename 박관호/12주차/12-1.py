# 초기 변수 설정
input_data = 5  # 입력 데이터의 초기값
weight = 3  # 가중치의 초기값
target = 8  # 목표값 (실제값)
learning_rate = 0.1  # 학습률

# 예측값 계산
pred = weight * input_data

# 예측값과 실제값의 차이 (오차) 계산
error = pred - target
print("original error : ", error)  # 초기 오차 출력

# 기울기 (slope) 계산
slope = 2 * input_data * error
print("slope : ", slope)  # 기울기 출력

########################################################

# 새로운 가중치 계산
new_weight = weight - learning_rate * slope
print("new weight : ", new_weight)  # 새로운 가중치 출력

# 새로운 예측값 계산
new_pred = new_weight * input_data

# 새로운 예측값과 실제값의 차이 (새로운 오차) 계산
new_error = new_pred - target
print("new error : ", new_error)  # 새로운 오차 출력

# 새로운 기울기 (slope) 계산
new_slope = 2 * input_data * new_error
print("new_slope : ", new_slope)  # 새로운 기울기 출력
