input_data = 5
weight = 3
target = 8

learning_rate = 0.01

pred = weight * input_data  #예측

error = pred - target       #오차 구하기
print("original error:", error)

slope = 2 * input_data * error  #기울기 구하기
print("slope:", slope)

new_weight = weight - learning_rate * slope #새로운 가중치 구하기
print("new weight:",new_weight)

new_pred = new_weight*input_data    #새 예측 구하기
print("new prediction:", new_pred)

new_error = new_pred - target       #새 오차 구하기
print("new error:", new_error)