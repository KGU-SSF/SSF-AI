input_data = 5  #입력값 
weight = 3  #가중치
target = 8  #목표

learning_rate = 0.1 #학습값
pred = weight * input_data #예측값

error = pred - target #오차 = 예측값 - 목표
print("original error : ", error)  #오차 출력

slope = 2 * input_data * error #기울기 = 2 * 입력값 * 오차
print("slope : ", slope)  #오차함수의 기울기 출력

new_weight = weight - learning_rate * slope #새로운 가중치 = 가중치 - 학습값 * 기울기
print("new weight : ", new_weight) #새로운 가중치 출력

new_pred = new_weight * input_data #새로운 예측값 = 새로운 가중치 * 입력값
print("new pred : ", new_pred)#새로운 예측값 출력

new_error = new_pred - target #새로운 오차 = 새로운 예측값 - 목표
print("new error : ", new_error) #새로운 오차 출력
