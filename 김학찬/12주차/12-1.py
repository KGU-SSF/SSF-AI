import numpy as np

input_data = 5
weight = 3
target = 8
learning_rate = 0.1

pred = weight * input_data  # weight(가중치)와 input_data를 곱하여 처음 예측 값 계산
error = pred - target   # 예측 값에서 못표 값을 빼서 오차를 계산
print("original error",error)   # 오차 출력

slope = 2 * input_data * error  # 기울기 계산
print("slope",slope)

new_weight = weight - learning_rate * slope # 기울기와 learning_rate를 이용하여 새로운 가충지(new_weight) 생성
print("new weight",new_weight)

new_pred = new_weight * input_data  # new_weight(오차를 고려하여 새롭게 생성된 가중치)와 input_data를 이용하여 새로운 예측 값 생성
print("new prediction",new_pred)

new_error = new_pred - target # new_pred(새로운 예측값)과 target(목표 값)을 빼서 새로운 오차를 계산
print("new error",new_error)    
                              # 위 과정을 반복할 수록 오차는 줄어들고 pred(예측 값)은 target(목표 값)에 가까워짐
