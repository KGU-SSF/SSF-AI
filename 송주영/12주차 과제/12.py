input_data = 5
weight =3
target = 8
learning_rate = 0.1

pred = weight * input_data
error = pred - target

#오차
print("originial error: ", error)

#기울기
slope = 2 * input_data * error
print("slope:", slope)

#새로운 가중치
new_weight = weight - learning_rate
print("new weight: ", new_weight)

#새로운 예측값
new_pred = new_weight * input_data
print("new prediction", new_pred)

#새로운 오차
new_error = new_pred - target
print("new error: ", new_error)