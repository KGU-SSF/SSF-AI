input_dada = 5 
weight = 3 #가중치
target = 8 #실제값
learning_rate = 0.1 #학습률

pred = weight * input_dada

error = pred - target #오차
print("original error:", error)

slope = 2 * input_dada * error #오차함수의 기울기
print("slope:", slope)

nwe_weight = weight - learning_rate * slope #새로운 가중치
print("new weight:", nwe_weight)

new_pred = nwe_weight * input_dada #새로운 예측값
print("new prediction:", new_pred)

new_error = new_pred - target #새로운 오차
print("new error:", new_error)