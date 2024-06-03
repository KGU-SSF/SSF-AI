input_data = 5 #입력값
weight = 3 #가중치
target = 8 #목표값
learning_rate = 0.1 #학습률
pred = weight * input_data #예측값 계산 : 3 x 5 = 15

error = pred - target #오차 계산 : 15 - 8 = 7
print("original error:", error) #위 계산 결과에 따라 원래 오차인 7이 출력되어짐

slope = 2* input_data * error #계산 : 2 x 5 x 7 = 70 
print("slope:", slope) #위 계산 결과에 따라 70이 출력되어짐

new_weight = weight-learning_rate * slope #계산 : 3 - 0.1 x 70 = -4.0
print("new_weight:", new_weight) #새로운 가중치 출력

new_pred = new_weight * input_data #계산 : -4.0 x 5 = -20.0
print("new prediction:", new_pred) #새로운 예측값 출력

new_error = new_pred- target #계산 : -20.0 - 8 = -28.0
print("new_error:", new_error) # 새로운 오차 출력