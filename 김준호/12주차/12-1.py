input_data = 5
weight = 3
target = 8
learning_rate = 0.1

pred = weight * input_data  # 기본 계산 : 가중치 * 입력값

error = pred - target # 오차 = abs(예측값 - 실제값)
print("orginal error:", error)

slope = 2 * input_data * error # 기울기 = 2 * 입력값 * 오차
print("slope:", slope)

new_weight = weight - learning_rate * slope # 가중치 update : 가중치 - 학습률 * 기울기
print("new weight:", new_weight)

new_pred = new_weight * input_data  
print("new prediction:", new_pred)

new_error = new_pred - target # 새 예측값 - 실제값
print("new error:", new_error)