input_data = 5 # 입력데이터 = 5
weight = 3 # 초기 가중치 = 3
target = 8 # 실제 값 = 8
learning_rate = 0.1 # 학습률 = 0.1

pred = weight * input_data # 예측 값 계산, 예측 값 = 초기 가중치 * 입력데이터

error = pred - target  # 오차 계산, 오차 = 예측 값 - 실제 값
print("original error:", error)

slope = 2 * input_data * error # 오차함수의 기울기 계산, 기울기 = 2 * 입력데이터 * 오차
print("slope:", slope)

new_weight = weight - learning_rate * slope #새로운 가중치= 기존 가중치 - 학습률 * 기울기
print("new weight:", new_weight)

new_pred = new_weight * input_data # 새로운 예측 값 계산, 새로운 예측 값 = 새로운 가중치 * 입력데이터
print("new prediction:", new_pred)

new_error = new_pred - target # 새로운 오차 계산, 새로운 오차 = 새로운 예측값 - 실제 값
print("new error:", new_error)