input_data = 5            # 입력 데이터
weight = 3                # 초기 가중치
target = 8                # 목표 값 
learning_rate = 0.1       # 학습률

pred = weight * input_data   # 예측 값 계산
# pred = 3 * 5 = 15

error = pred - target        # 예측 값과 목표 값의 차이 (오차)
print("original error:", error)
# original error: 15 - 8 = 7

slope = 2 * input_data * error  # 오차를 줄이기 위한 기울기 계산
print("slope:", slope)
# slope = 2 * 5 * 7 = 70

new_weight = weight - learning_rate * slope  # 새로운 가중치 계산
print("new weight:", new_weight)
# new_weight = 3 - 0.1 * 70 = -4

new_pred = new_weight * input_data  # 새로운 가중치로 예측 값 계산
print("new prediction:", new_pred)
# new_pred = -4 * 5 = -20

new_error = new_pred - target  # 새로운 예측 값과 목표 값의 차이 (새로운 오차)
print("new error:", new_error)
# new error: -20 - 8 = -28