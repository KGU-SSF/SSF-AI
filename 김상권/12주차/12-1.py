input_data = 5
weight = 3 
target = 8
learning_rate = 0.1

pred = weight * input_data #예측 값 (3 * 5 = 15)

error =pred - target #오차 값 (15 - 8 = 7)
print("original error:", error)

slope = 2 * input_data * error #오차함수의 기울기 (2 * 5 * 7 = 70)
print("slope:", slope)

new_weight = weight - learning_rate * slope #새로운 가중치 (3 - 0.1 * 70 = -4)
print("new weight:", new_weight)

new_pred = new_weight * input_data #새로운 예측 값 (-4 * 5 = -20)
print("new prediction:", new_pred)
 
new_error = new_pred - target #새로운 오차 값 (-20 - 8 = -28)
print("new error:", new_error)
 