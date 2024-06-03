input_data = 5
weight = 3
target = 8
learning_rate = 0.1

pred = weight*input_data

error = pred - target #오차
print("original error:",error)

slope=2*input_data*error #기울기
print("slope:",slope)

new_weight=weight-learning_rate*slope #원래 가중치에서 뺌
print("new weight:",new_weight) #새로운 가중치

new_pred=new_weight*input_data #예측값 계산
print("new prediction:", new_pred)

new_error=new_pred-target #새 오차 계산
print("new error:",new_error)