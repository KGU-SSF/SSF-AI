input_data = 5 #입력값 설정
weight = 3  #가중치 설정
target = 8  #실제값 설정
learning_rate = 0.1 #학습률 설정

pred = weight * input_data #예측값 설정 (가중치 * 입력값)
error = pred - target #오차 설정 (예측값 - 실제값)
print("original error : ", error) #7

slope = 2 * input_data * error #기울기 설정 (2 * 입력값 * 오차)
print("slope : ",slope) #70

new_weight = weight - learning_rate * slope #새로운 가중치 설정(학습률 * 기울기)
print("new weight : ", new_weight) #-4

new_pred = new_weight * input_data #새로운 예측값 설정(가중치 - 새로운 가중치 * 입력값)
print("new prediction : ", new_pred)#-20

new_error = new_pred - target #새로운 오차값 설정(새로운 예측값 - 실제값)
print("new error : ", new_error) #-28
