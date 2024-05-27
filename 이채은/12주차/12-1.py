input_data = 5 #입력 데이터 설정
weight = 3 #가중치 설정
target = 8 #목표 값 설정

learning_rate = 0.1 #학습률 설정

pred = weight * input_data #초기 예측 값 계산
error = pred - target #오차 계산
print("original error:", error) #초기 오차 값 출력

slope = 2 * input_data * error #입력 데이터와 오차를 사용하여 기울기 계산
print("slope:", slope) #계산된 기울기 출력

new_weight = weight - learning_rate * slope #경사하강법을 사용하여 가중치 업데이트
print("new weight:", new_weight) #업데이트된 가중치 값 출력

new_pred = new_weight * input_data #업데이트된 가중치와 입력 데이터를 사용하여 새로운 예측 값 계산
print("new prediction:", new_pred) #계산된 새로운 예측 값 출력

new_error = new_pred - target #새로운 예측 값에서 목표 값을 빼서 새로운 오차 값 계산
print("new error:", new_error) #새로운 오차 값 출력