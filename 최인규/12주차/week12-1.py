input_data = 5 # 입력 데이터
weight = 3 # 가중치 초기값
target = 8 # 목표값
learning_rate = 0.1 # 학습률

pred = weight * input_data # 현재 예측값 계산

error = pred - target # 예측값과 목표값의 차이(오차) 계산
print("original error:", error) # 초기 오차 출력

slope = 2 * input_data * error # 오차에 대한 기울기 계산
print("slope:", slope) # 기울기 출력

new_weight = weight - learning_rate * slope # 새로운 가중치 계산 (경사 하강법)
print("new weight:", new_weight) # 새로운 가중치 출력

new_pred = new_weight * input_data # 새로운 예측값 계산
print("new predicition:", new_pred) # 새로운 예측값 출력

new_error = new_pred - target # 새로운 오차 계산
print("new error:", new_error) # 새로운 오차 출력
