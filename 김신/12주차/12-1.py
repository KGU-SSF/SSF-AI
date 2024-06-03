input_data = 5 #입력 값
weight = 3 #초기 가중치 = 5
target = 8 #목표 값 = 8
learning_rate = 0.1 #학습률

pred = weight * input_data #예측값 = 입력값 * 가중치

# error = 오차값
error = pred - target #예측값 - 실제값
print("original error:", error)

# slope = 기울기
slope = 2 * input_data * error #기울기 = 2 * 입력값 * 오차
print("slope :", slope)

new_weight = weight - learning_rate * slope #새로운 가중치 = 가중치 - 학습률
print("new weight:", new_weight)

new_pred = new_weight * input_data #새로운 예측값 = 새로운 가중치 * 입력값
print("new prediction:", new_pred)

new_error = new_pred - target #새로운 오차 = 새로운 예측값 - 실제값
print("new error :", new_error)