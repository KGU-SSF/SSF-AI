input_data = 5
weight = 3
target = 8
learning_rate = 0.1

pred = weights * input_data

error = pred - target
print("original error:", error)

slope = 2 * input_data * error #slope 기울기
print("slope:", slope)

new_weight = weight - learning_rate * slope #새로운 가중치
print("new weight:", new_weight)

new_pred = new_weight * input_data #새로운 예측값
print("new prediction:", new_pred)

new_error = new_pred - target #새로운 오차
print("new error:", new_error)
