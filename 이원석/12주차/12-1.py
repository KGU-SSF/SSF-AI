input_data = 5
weight = 3
target = 8
learning_rate = 0.1

pred = weight * input_data
error = pred - target # 오차는 예측값과 목표값의 차이
print("original error:", error)

slope = 2 * input_data * error # 오차함수의 기울기 오차를 가중치에 대해 미분한 값
print("slope:", slope)

new_weight = weight - learning_rate * slope #새로운 가중치는 현재 개중치에서 학습률과 기울기의 곱을 뺀 값
print("new prediction:", new_weight)

new_pred = new_weight * input_data
print("new prediction:", new_pred)

new_error = new_pred - target # 새로운 오차는 새로운 예측값 빼기 목표값
print("new error", new_error) 

#오차는 실제에서 예측을 빼는거랑 예측에서 실제를 빼는 것 상관 없다 -> 어차피 제곱할거여서
#slope는 인풋과 에러를 곱해서 2를 곱함