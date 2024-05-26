input_data = 5 # 입력값 5
weight = 3 # 가중치 3
target = 8 # 정답 8
learning_rate = 0.1 # 학습빈도 0.1(가중치의 조정 정도)

pred = weight * input_data # 가중치 * 입력값 = 예측값

error = pred - target # 예측값 - 정답 = 오차
print("error:", error) # 1차 오차 출력

slope = 2 * input_data * error # 2 * 입력값 * 오차 = 오차함수의 기울기 (y' = 2x * error);mse를 이용하므로 오차함수가 x^2라고 했을 때 그 미분값인 2x가 오차함수의 기울기임
print("slope:", slope) # 오차함수의 기울기 출력

new_weight = weight - learning_rate * slope # (가중치 - 학습빈도) * 기울기 = 새로운 가중치
print("new weight:", new_weight) # 새로운 가중치 출력

new_pred = new_weight * input_data # 새로운 가중치 * 입력값 = 새로운 예측값
print("new prediction:", new_pred) # 새로운 예측값 출력

new_error = new_pred - target # 새로운 예측값 - 정답 = 새로운 오차
print("new error:", new_error) # 새로운 오차 출력