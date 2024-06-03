#예측 - 실제 / 실제 - 예측이 상관없는 이유 어짜피 제곱해서
input_data = 5
weight = 3
target = 8
learning_rate = 0.1
pred = weight * input_data

error = pred - target
print("original error:", error)

slope = 2 * input_data * error #기울기
print("slope:", slope)

new_weight = weight - learning_rate * slope #새로운 가중치 업데이트/정의(원래 있던 가중치에서 learning_rate*기울기를 뺀것)
print("new weight:", new_weight)

new_pred = new_weight * input_data #새로운 가중치에 따른 prediction
print("new prediction",new_pred)

new_error = new_pred - target #새로운 가중치에 따른 error
print("new error:", new_error)

