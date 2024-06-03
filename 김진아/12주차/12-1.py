input_data = 5
weight = 3
target = 8
learning_rate = 0.1

pred = weight * input_data #초기 예측값

error = pred - target
print("original error:", error) #오차

slope = 2 * input_data * error
print("slope:", slope) #기울기

new_weight = weight - learning_rate * slope
print("new weight:", new_weight) #새로운 가중치

new_pred = new_weight * input_data
print("new prediction:", new_pred) #새로운 예측값 계산

new_error = new_pred - target
print("new error:", new_error) #새로운 오차