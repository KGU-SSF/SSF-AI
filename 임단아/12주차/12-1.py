input_data = 5
weight = 3
target = 8
lerning_rate = 0.1

pred = weight * input_data #예측값 계산

error = pred - target #오차 계산
print("originial error : ", error)

slope = 2 * input_data * error #기울기 계산
print("slope : ", slope)

new_weight = weight - learning_weight * slope #새로운 가중치로 변경
print("new weight : ", new_weight)

new_pred = new_weight * input_data #새로운 예측값을 계산
print("new prediction : ", new_pred)

new_error = new_pred - target #새로운 오차 계산
print("new error : ", new_error)